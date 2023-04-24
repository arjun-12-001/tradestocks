# from tradingview_ta import TA_Handler, Interval, Exchange
# import pandas as pd 

# symbols=[]
# data = pd.read_csv("names.csv")
# data.drop(columns=["NAME OF COMPANY"],inplace = True)
# symbols = data.values.tolist()
# for symbol in symbols:
#   output = TA_Handler(
#       symbol=symbol[1],
#       screener="india",
#       exchange="NSE",
#       interval=Interval.INTERVAL_1_MINUTE
#   )
#   try:
#     info = output.get_analysis().summary
#     if info["RECOMMENDATION"] == "BUY" and info["BUY"]>10:
#      print("company symbol : "+symbol[1])
#      print(output.get_analysis().summary)
#   except:
#     print("sorry error in fetching....")
from deta import Deta
import os
from dotenv import load_dotenv

load_dotenv(".env")

keyval = os.getenv("keyval")
deta = Deta(keyval)
db =deta.Base("new_userDB")

def insert_user(username,name, password):
    return db.put({"key": username,"name": name, "password": password}) 

def fetch_users():
    res = db.fetch()
    return res.items

def get_user(username):
    return db.get(username)


# insert_user("Arjun","Ronin001","12345")
# insert_user("Chris","chris_boi","12345")
# insert_user("Lakshmi","laksmi420","12345")
# insert_user("Sivaram","SRK2023","12345")

val = fetch_users()
for i in val:
    print(i["key"],i["password"])
# users = fetch_users()
# listed = [user["password"] for user in users]
# print(listed)