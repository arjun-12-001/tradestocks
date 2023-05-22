import streamlit as st 
import pandas as pd
import yfinance as yf
import pandas_ta as ta
import plotly.express as px
from scipy.signal import argrelextrema
import numpy as np 
import strats 
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import tradingview as tv
import stonks
import MLchek as ml
import tradingview as tv
import time
from sklearn.neighbors import KernelDensity

def bullish_func(df):
  length = len(df)
  high = list(df['High'])
  date = list(df.index  )
  low = list(df['Low'])
  close = list(df['Close'])
  open = list(df['Open'])
  days = []
  for i in range(1,length):
    if open[i-1] > close[i-1]:
      if close[i] > open[i]:
          if close[i] >= open[i-1]:
              if close[i-1] >= open[i]:
                  if close[i] - open[i] > open[i-1] - close[i-1]:
                      days.append(date[i])
                  else:
                      pass
              else:
                  pass
          else:
              pass
      else:
          pass
  else:
      pass
  return days

def resist_supp(data):
    sample_val = data.iloc[-50:]
    sample = data.iloc[-50:]["Close"].to_numpy().flatten()
    sample_original = sample.copy()
    maxima = argrelextrema(sample,np.greater)
    minima = argrelextrema(sample,np.less)
    extrema = np.concatenate((maxima,minima), axis=1)[0]
    extrema_prices = np.concatenate((sample[maxima],sample[minima]))
    initial_price = extrema_prices[0]
    kde = KernelDensity(kernel="gaussian", bandwidth = initial_price/2000).fit(extrema_prices.reshape(-1,1))
    a,b = min(extrema_prices),max(extrema_prices)
    price_range = np.linspace(a,b,1000).reshape(-1, 1)
    pdf = np.exp(kde.score_samples(price_range))
    peaks = find_peaks(pdf)[0]
    new = price_range[peaks].tolist()
    flatten_list = [num for sublist in new for num in sublist]
    new = flatten_list
    return new

def least(new,price):
    min = abs(price[0]-new)
    diff = min

    for i in range(len(price)):
        val=abs(price[i]-new)
        
        if val<diff:
            diff = val
            min = price[i]
    return min   

def buy_sell(df):
    signalBuy = []
    signalSell = []
    position = False 

    for i in range(len(df)):
        if df['SMA 20'][i] > df['SMA 50'][i]:
            if position == False :
                signalBuy.append(df['Close'][i])
                signalSell.append(np.nan)
                position = True
            else:
                signalBuy.append(np.nan)
                signalSell.append(np.nan)
        elif df['SMA 20'][i] < df['SMA 50'][i]:
            if position == True:
                signalBuy.append(np.nan)
                signalSell.append(df['Close'][i])
                position = False
            else:
                signalBuy.append(np.nan)
                signalSell.append(np.nan)
        else:
            signalBuy.append(np.nan)
            signalSell.append(np.nan)
    return pd.Series([signalBuy, signalSell])

st.subheader("Resistence and Support Bands ")
st.sidebar.subheader("Select Company")
companies = stonks.comp(1)
option = st.sidebar.selectbox('', options = companies)
val1 = stonks.comp(3,option)
symbol = str(val1)+".NS"
tick = symbol.lower()
data = yf.download(tick,period="1y")
st.write("last traded price")
st.write(data.Close[-1])
res_sup = resist_supp(data)
val = least(data.Close[-1],res_sup)
if val > data.Close[-1]:
    st.write("Nearest resistence : " +str(val))
else:
    st.write("Nearest support : " +str(val))

st.title("Technical Analysis")
Bull_Engulfing,rsi,macd=st.tabs(["Bullish Engulfing","RSI","MACD"])

with Bull_Engulfing:
    pass
    # path = r"C:\Users\Arjun Ramesh\OneDrive\Desktop\portfolio\names_new.csv"
    # data = pd.read_csv(path)
    # data.drop(columns=['Unnamed: 0'],axis=1,inplace=True)
    # comp = data['Company Name'].tolist()
    # sym = data['Symbol'].tolist()
    # new_val = {c:s for c,s in zip(comp,sym)}

    # rejected = []
    # for i in new_val:
    #     symbol = new_val[i]+'.NS'
    #     df = yf.download(symbol,period='5mo')
    #     st.write("company : "+i)
    #     days = bullish_func(df)
    #     for i in range(len(days)):
    #         # days[i]=days[i].date().strftime("%Y-%m-%d")
    #         if days[i].date().strftime("%Y-%m-%d").startswith('2023-04'):
    #             days[i] = days[i].date().strftime("%Y-%m-%d")
    #         else:
    #             days[i]='0'
    #     while '0' in days:
    #         days.remove('0')
    # st.write(days)
RSI_val = pd.DataFrame()
with rsi:

    period  = st.text_input('Time Period', placeholder="eg:1y,1mo,1d")
    df = pd.DataFrame().ta.ticker(ticker=tick,period=period)
    try:
        st.write(df)
        RSI  = df.ta.rsi(period=14)
        df.drop(columns=['Dividends','Stock Splits'],inplace = True)
        df["RSI"] = RSI
        RSI_val = RSI
        df.dropna(inplace = True)
        fig = px.line(x=df.index,y=df["RSI"])
        fig.add_hline(y=0,line_color='#edc',line_width=4)
        fig.add_hline(y=100,line_color='#edc',line_width=4)
        fig.add_hline(y=70,line_color='#e60b0b',line_width=3)
        fig.add_hline(y=30,line_color='#05f725',line_width=3)
        fig.update_layout(title=tick + " : RSI Indicator with Overbought and oversold Signals", yaxis_title='Close Price INR (₨)', legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))
        st.plotly_chart(fig)
    except:
       pass

MACD_val = pd.DataFrame()
with macd:
    try:
        
        period2  = st.text_input('Time Period', placeholder="ie : 1y,1mo,1d")
        df = pd.DataFrame().ta.ticker(ticker=tick,period=period2)
        st.write(df)
        df['SMA 20'] = ta.sma(df['Close'],20)
        df['SMA 50'] = ta.sma(df['Close'],50)
        df.dropna(inplace=True)
        df['Buy_Signal_price'], df['Sell_Signal_price'] = buy_sell(df)
        MACD_val = df[["Buy_Signal_price","Sell_Signal_price"]]
        fig = px.line(df, x=df.index, y=['Close', 'SMA 20', 'SMA 50'], color_discrete_sequence=['blue', 'green', 'red'])
        fig.add_scatter(x=df[df['Buy_Signal_price'].notnull()].index, y=df['Buy_Signal_price'][df['Buy_Signal_price'].notnull()], name='Buy', mode='markers', marker=dict(symbol='triangle-up', color='yellow', size=8, line=dict(width=1, color='Black')))
        fig.add_scatter(x=df[df['Sell_Signal_price'].notnull()].index, y=df['Sell_Signal_price'][df['Sell_Signal_price'].notnull()], name='Sell', mode='markers', marker=dict(symbol='triangle-down', color='red', size=8, line=dict(width=1, color='Black')))
        fig.update_layout(title=tick + " : MACD Indicator with buy and sell signals", yaxis_title='Close Price INR (₨)', legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))
        st.plotly_chart(fig)
        
    except:
        pass
st.subheader("Analysis on Trending Stocks:")

# model.passing_func(MACD_val,RSI_val)
symbol = tv.week_52()
for i in symbol:
    st.write("Stock Symbol : ",i.strip('.ns'))
    cl,v20,v50 = strats.run_ema(i)
    st.write(f'<span style="color: blue;">Last Close Price : {cl}</span>', unsafe_allow_html=True)
    st.write(f'<span style="color: green;">20 Moving Average : {v20}</span>', unsafe_allow_html=True)
    st.write(f'<span style="color: red;">50 Moving Average : {v50}</span>', unsafe_allow_html=True)

st.subheader("Equity Price forecasting")
st.write("ML model takes time to forecast,Please wait.....")
symbol = tv.week_52()
pres=None
fut=None
for company in symbol:
    comp = company.strip('.ns')
    button_clicked = st.button(company)
    if button_clicked:
        with st.spinner('Building Model...'):
            present,future = ml.model_run(company)
            pres=present
            fut=future
            time.sleep(30) 
        st.success('Loading complete!')
        plt.figure(figsize=(16, 8))
        plt.title(f'LSTM Model prediction for {comp}')
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Close Price USD ($)', fontsize=18)
        plt.plot(present['Close'])
        plt.plot(future['Close'])
        plt.legend(['Historical Prices', 'Predicted Prices'], loc='lower right')
        st.pyplot(plt.gcf())
        with st.expander("predicted future price : "):
            st.markdown(f'<span style="color: red;">Refer predicted prices with support/resistence</span>', unsafe_allow_html=True)
            st.write(future.Close)
            value,resis,suppo=tv.resi_supp(company)
            data = {
            'Date': value.index,
            'Close': value['Close'],
            'Support': suppo,
            'Resistance': resis
            }
            df = pd.DataFrame(data)
            st.line_chart(df.set_index('Date'))