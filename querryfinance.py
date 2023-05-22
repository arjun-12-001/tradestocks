import database as db
import yfinance as yf
# d1 = yf.download("hdfcbank.ns",period = "1d",interval='1h')
# price = float(d1.Close.tail(1).values)
# name = "hdfcbank.ns"
print(db.profits(3220,12,"eichermot.ns"))