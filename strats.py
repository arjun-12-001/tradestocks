import pandas as pd 
from bs4 import BeautifulSoup 
import requests
import pandas as pd
import yfinance as yf
import numpy as np
import pandas_ta as ta
import tradingview as tv

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

def run_ema(i):

    print(i)
    df = pd.DataFrame().ta.ticker(ticker=i,period="3mo")
    df['SMA 20'] = ta.sma(df['Close'],20)
    df['SMA 50'] = ta.sma(df['Close'],50)
    df.dropna(inplace=True)
    df['Buy_Signal_price'], df['Sell_Signal_price'] = buy_sell(df)
    MACD_val = df[["Buy_Signal_price","Sell_Signal_price"]]
    v20 = float(df["SMA 20"].tail(1).values)
    v50 = float(df["SMA 50"].tail(1).values)
    ck = float(df['Close'].tail(1).values)
    return ck,v20,v50

