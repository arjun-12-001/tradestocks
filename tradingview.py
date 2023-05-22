import pandas as pd 
from bs4 import BeautifulSoup 
import requests
import pandas as pd
import yfinance as yf
# import plotly.express as px
import pandas_ta as ta
import ta
# import matplotlib.pyplot as plt

# Download stock data
def resi_supp(symbol):
  stock_data = yf.download(symbol, period='2y', interval='1wk')

  # Compute support and resistance levels using ta-lib
  support_levels = ta.volatility.bollinger_lband(stock_data['Close'], window=20, window_dev=2)
  resistance_levels = ta.volatility.bollinger_hband(stock_data['Close'], window=20, window_dev=2)

  # Print the support and resistance levels
  print("Support levels:", support_levels.dropna(inplace=True))
  print("Resistance levels:", resistance_levels.dropna(inplace=True))
  weeks_close = stock_data['Close'].tail(1).mean()  
  support_val = support_levels.tail(1).mean()
  resistence_val = resistance_levels.tail(1).mean()
  return stock_data,resistance_levels,support_levels
  # # Plot the support and resistance levels
  # plt.plot(stock_data.index, stock_data['Close'], label="Close")
  # plt.plot(support_levels.index, support_levels, label="Support")
  # plt.plot(resistance_levels.index, resistance_levels, label="Resistance")
  # plt.legend()
  # plt.show()
def week_52():
  html_text=requests.get('https://www.icicidirect.com/equity/market-today/52-week-high/nse/nifty-100/intraday').text
  soup = BeautifulSoup(html_text, 'lxml')
  table = soup.find_all('td',class_ ='company_name')
  i=1
  names = []
  for row in table:  
    if(i<=15):
      stock_name = row.find('span').text
      stock_name = stock_name + '.'
      names.append(stock_name)
      i=i+1
    else:
      break

  df = pd.read_csv("names_new.csv")
  df.drop(columns=["Unnamed: 0"],inplace=True)
  df = df.values.tolist()
  symbol=[]
  for i in df:
    if i[0] in names:
      i[1]=i[1]+'.ns'
      symbol.append(i[1])
  return symbol

def top_gainer():
  html_text=requests.get('https://www.icicidirect.com/equity/market-today/top-gainers/nse/nifty-100/week').text
  soup = BeautifulSoup(html_text, 'lxml')
  table = soup.find_all('td',class_ ='company_name')
  i=1
  names = []
  for row in table:  
    if(i<=15):
      stock_name = row.find('span').text
      stock_name = stock_name + '.'
      names.append(stock_name)
      i=i+1
    else:
      break

  df = pd.read_csv("names_new.csv")
  df.drop(columns=["Unnamed: 0"],inplace=True)
  df = df.values.tolist()
  symbol=[]
  for i in df:
    if i[0] in names:
      i[1]=i[1]+'.ns'
      symbol.append(i[1])
  return symbol

def volume():
  html_text=requests.get('https://www.icicidirect.com/share-market-today/most-active-by-volume/nse/nifty-100/week').text
  soup = BeautifulSoup(html_text, 'lxml')
  table = soup.find_all('td',class_ ='company_name')
  i=1
  names = []
  for row in table:  
    if(i<=15):
      stock_name = row.find('span').text
      stock_name = stock_name + '.'
      names.append(stock_name)
      i=i+1
    else:
      break

  df = pd.read_csv("names_new.csv")
  df.drop(columns=["Unnamed: 0"],inplace=True)
  df = df.values.tolist()
  symbol=[]
  for i in df:
    if i[0] in names:
      i[1]=i[1]+'.ns'
      symbol.append(i[1])
  return symbol

names = week_52()
print(names)