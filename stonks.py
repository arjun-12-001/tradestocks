# -*- coding: utf-8 -*-
"""stonks

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p9_aQqrufoDcr726_bYyLQFGu17ObrP-
"""

pip install nsetools

from nsetools import Nse
import pandas as pd,numpy as np

nse=Nse()

q=nse.get_quote('infy')
q

pip install yfinance

import yfinance as yf
import pandas as pd

data = yf.download("CIPLA.NS")
data

sym_names = {}
data = pd.read_csv("EQUITY_L.csv")
symbols = data["SYMBOL"]
comp_names = data["NAME OF COMPANY"]
count = 0
for comp_name in comp_names:
  sym_names[comp_name] = symbols[count]
  count = count + 1 
print(sym_names)

possible = []
string = input("enter the company name : ").lower()
substr = data["NAME OF COMPANY"].tolist()
for comp in substr:
  if comp.lower().startswith(string):
    possible.append(sym_names[comp])
possible

for symbol in possible:
  val = symbol+'.NS'
  nigg = yf.download(val)
  print(val)
  print(nigg)