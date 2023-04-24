import streamlit as st, pandas as pd, numpy as np, yfinance as yf
import plotly.express as px
from stocknews import StockNews
import querryfinance as qf
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from GoogleNews import GoogleNews
import streamlit_authenticator as stauth
import stonks
from streamlit_lottie import st_lottie
import os,requests,json
import streamlit_authenticator as stauth 
from yahooquery import Ticker
import pandas as pd 


st.title("Stock Portfolio Dashboard")
try:
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)
except:
    pass

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_i2eyukor.json")

path = os.path.abspath("lottiefiles/animate.json")
lottie_coding = load_lottiefile(path)

st_lottie(lottie_hello,key="hello",height=400,width=400)

with st.expander("Description"):
    st.markdown(""" 
        -This Dahboard allows you to selct a necessary stock you wish to proceed to buy or sell and 
        alalytics are done necessarily
    """)

try:
    st.sidebar.subheader("Select Company")
    companies = stonks.comp(1)
    option = st.sidebar.selectbox('', options = companies)
    val1 = stonks.comp(3,option)
    symbol = str(val1)+".NS"
    ticker = symbol.lower()

    start_date = st.sidebar.date_input("Start Date")
    end_date = st.sidebar.date_input("End Date")
   
    if start_date == end_date:
        st.write("Please select atleast 1 week Timespan")
    else:
        data =yf.download(ticker,start=start_date,end=end_date)
        fig = px.line(data,x = data.index,y=data["Adj Close"],title=ticker)
        st.plotly_chart(fig)

        pricing_data, related_top_stocks, news = st.tabs(["Pricing Data","Fundamental Data", "Top 10 News"])

        with pricing_data:
            st.write("Price Tracking :",ticker)
            d2 = data
            d2["% Change"] = data["Adj Close"]/data["Adj Close"].shift(1)-1
            d2.dropna(inplace=True)
            st.write(d2)
            annual_ret = d2["% Change"].mean()*25200
            st.write("Annual Return : ",annual_ret,"%")
            stdev = np.std(d2["% Change"])*np.sqrt(252)
            st.write("Standard Devoiation : ",stdev*100,"%")
            st.write("Risk Adj. Return : ",annual_ret/(stdev*100))

        with related_top_stocks:
            try:
                comps = pd.read_csv("names_new.csv")
                good_ones = []
                for comp in comps["Symbol"]:
                    symbol = comp+".NS"
                    data = Ticker(symbol)
                    val = data.financial_data
                    if val[symbol]["recommendationKey"] == "strong_buy":
                        good_ones.append(symbol)
                for i in good_ones:
                    st.write(i)
                    data = Ticker(i).summary_detail
                    for i in data['SBIN.NS']:
                        if data["SBIN.NS"][i] != None:
                            print(str(i) +" : "+str(data["SBIN.NS"][i]))
            except:
                pass


        with news:
            try:
                gn = GoogleNews(lang='en',region='India',period='7d')
                name = ticker.replace('.ns','')
                analyzer = SentimentIntensityAnalyzer()
                searching = name + ' company india'
                print(searching)
                gn.search(searching)
                overall = 0
                pos = 0
                neg = 0

                for i in gn.result():
                    st.write("-----------------------------------------------")
                    st.write(i['date'])
                    st.write(i['title'])
                    st.write(i['desc'])

                    text = i['desc']
                        # Create an instance of SentimentIntensityAnalyzer

                        # Analyze the sentiment of a text
                    scores = analyzer.polarity_scores(text)

                        # Extract sentiment scores
                    compound_score = scores['compound']
                    positive_score = scores['pos']
                    negative_score = scores['neg']
                    neutral_score = scores['neu']
                    overall = overall + compound_score
                        

                        # Print the sentiment scores
                    st.write('Compound Score:', compound_score)
                    st.write('Positive Score:', positive_score)
                    st.write('Negative Score:', negative_score)
                    st.write('Neutral Score:', neutral_score)
                st.write("-----------------------------------------")
                st.write("Overall outloot on ",searching)
                st.write(overall)
                values = st.slider('News Rating',0.0, 10.0,overall)
                
            except:
                st.write("news was not fetched")
except:
    pass

st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    # renderer="svg", # canvas
    height=720,
    width=720,
    key=None,
    )
