#this module is used to fetch the company details desired by the consumer  
import stonks as sto
import yfinance as yf
from datetime import datetime

def select_comp():
    symbols,companies = sto.comp()

    print("""\nchoose the company 
        ------------------------   """)
    for no,company in enumerate(companies):
        print(str(no+1)+": "+company)

    choice = int(input("enter the company serial number you like to pick : "))
    sd = datetime(int(input("enter start date(yyyy, mm, dd)")))
    ed = datetime(int(input("enter end date(yyyy, mm, dd)")))
    inter = input("enter time interval (1m,1h,1d)")
    # for symbol in symbols:
    val = symbols[choice-1]+'.NS'
    nigg = yf.download(tickers=val,start=sd,end=ed,interval=inter)
    return companies[choice-1],nigg