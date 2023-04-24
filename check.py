from turtle import pd
import streamlit as st
import plotly_express as px
import plotly.graph_objects as go
import pandas as pd
import stonks
import numpy as np
import json
import datetime
import requests 
from streamlit_lottie import st_lottie
import os
import yfinance as yf

st.set_page_config(layout="wide")

st.title("Portfolio Dashboard")

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
# ----------------------------------------------------------------------------
with st.expander("Description"):
    st.markdown(""" 
    -This Dahboard allows you to selct a necessary stock you wish to proceed to buy or sell and 
    alalytics are done necessarily
""")

with st.expander("Information Box"):
    pricing_data, fundamental_data, news = st.tabs(["Pricing Data","Fundamental Data", "Top 10 News"])
    
    with pricing_data:
        b1 = st.button("Equity information")     
    with fundamental_data:
        b2 = st.button("Number of Investments")
    with news:
        b3 = st.button("Return of Investments")

st.sidebar.subheader("Select Company")
companies = stonks.comp(1)
option = st.sidebar.selectbox('', options = companies)
#comp name = option , symbol = val
val1 = stonks.comp(3,option)
symbol = str(val1)+".NS"
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")

graph = st.sidebar.button("Launch "+option+" Graph")

if val1 is not None:
    data = yf.download(symbol,start=start_date,end=end_date)
    st.markdown("stock price of "+option)
    st.write(data.tail(10))    

# def datechange(d1,d2):
if graph:
    # st.line_chart(data["Close"])  
    fig = px.line(data,x = data.index,y=data["Adj Close"],title=data)
    st.plotly_chart(fig)    

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
