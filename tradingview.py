import yfinance as yf
import pandas as pd 
from tradingview_ta import TA_Handler, Interval, Exchange
import pandas as pd 

comps = pd.read_csv("names_new.csv")
name = []
for comp in comps["Symbol"]:
  symbol = comp+".NS"
  data = yf.Ticker(symbol)
  hist = data.history(period="3d")
  # hist_mean = hist["Volume"].iloc[1:3:1].mean().astype(int)
  hist1 = hist["Volume"].iloc[0]
  hist2 = hist["Volume"].iloc[1]
  hist3 = hist["Volume"].iloc[2]
  if (hist3 > hist2 > hist1):
    name.append(symbol)
# -----------------
print(name)
# -----------------
for x in name:
  d1 = yf.Ticker(x)
  hist0 = d1.history(period="1mo")
  print(x)
  val = pd.DataFrame(hist0[["Close","Volume"]])
  val.reset_index(inplace=True)
  val['Date'] = pd.to_datetime(val['Date']).dt.date
  graph = val[["Date","Close"]].iloc[-10:]
  # graph.set_index("Date",inplace=True)
  # graph.plot.line(y="Close",use_index=True)

# --------------------------
# --------------------------

listed = []
symbols = []
df = pd.read_csv("names_new.csv")
df.drop(columns=["Company Name"],inplace = True)
symbols = df.values.tolist()
for symbol in symbols:
  output = TA_Handler(
      symbol=symbol[1],
      screener="india",
      exchange="NSE",
      interval=Interval.INTERVAL_1_MINUTE
  )

  try:
    info = output.get_analysis().summary
    if info["RECOMMENDATION"] == "NEUTRAL" :
      listed.append(symbol[1])
      print("company symbol : "+symbol[1])
      print(output.get_analysis().summary)
  except:
    pass