import streamlit as st, pandas as pd, numpy as np, yfinance as yf
import plotly.express as px
from stocknews import StockNews
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from GoogleNews import GoogleNews
import stonks
from streamlit_lottie import st_lottie
import os,requests,json
from yahooquery import Ticker
import plotly.graph_objs as go
import pandas as pd 
import tradingview as tv

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
to_ml = []# to pass to prophet model 
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
        st.subheader("Equity Outlook and Fundamentals")
        pricing_data, fundamental, news = st.tabs(["Pricing Data","Fundamental Data", "Top 10 News"])

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

        with fundamental:
            st.subheader("Stock to hold : ")
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
                    st.subheader("company : "+i)
                    with st.expander("Eqity Info"):
                        data = Ticker(i).summary_detail
                        for j in data[i]:
                            if data[i][j] != None:
                                st.write(str(j)+" : "+str(data[i][j]))
                to_ml = good_ones
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
    st.subheader("Stock Screener")
    gainers = tv.top_gainer()
    week_high = tv.week_52()
    vol = tv.volume()
    gain_val,week,volu = st.tabs(["Top Gainer","52 Week High","Volume Change"])
    with gain_val:
        d1 = {'Top Gainers':gainers}
        d1 = pd.DataFrame(d1)
        d1['Sl No'] = range(1, len(d1) + 1)
        d1.set_index(['Sl No'],inplace=True)
        st.table(d1)         
    with week:
        d2 = {'52 week high':week_high}
        d2 = pd.DataFrame(d2)
        d2['Sl No'] = range(1, len(d2) + 1)          
        d2.set_index(['Sl No'],inplace=True)
        st.table(d2)
    with volu:
        d3 = {'volume change':vol}
        d3 = pd.DataFrame(d3)
        d3['Sl No'] = range(1, len(d3) + 1)
        d3.set_index(['Sl No'],inplace=True)
        st.table(d3)
    
    # print(to_ml)
    # filter = ml.runsML(to_ml)
    # st.write("ML trend predicted stocks :")
    # st.write(filter)

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

