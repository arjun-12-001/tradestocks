from yahooquery import Ticker
import pandas as pd 

comps = pd.read_csv("names_new.csv")
good_ones = []
for comp in comps["Symbol"]:
  symbol = comp+".NS"
  data = Ticker(symbol)
  val = data.financial_data
  if val[symbol]["recommendationKey"] == "strong_buy":
    good_ones.append(symbol)
    print(symbol)

# for comp in comps["Symbol"]:
#     symbol = comp+".NS"
#     data = Ticker(symbol)
#     val2 = data.financial_data
#     print(val2)