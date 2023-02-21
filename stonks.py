# module used to collect list of companies from database and pass to companies module
import pandas as pd

def comp(val=0):
  if val == 1:
    data = pd.read_csv("EQUITY_L.csv")
    comp_names = data["NAME OF COMPANY"]
    return comp_names 
  else:    
    sym_names = {}
    data = pd.read_csv("EQUITY_L.csv")
    symbols = data["SYMBOL"]
    comp_names = data["NAME OF COMPANY"]
    count = 0

    for comp_name in comp_names:
      sym_names[comp_name] = symbols[count]
      count = count + 1 
    print(sym_names)

    possible1 = []
    possible2 = []
    string = input("enter the company name : ").lower()
    substr = data["NAME OF COMPANY"].tolist()
    for comp in substr:
      if comp.lower().startswith(string):
        possible1.append(sym_names[comp])
        possible2.append(comp)
    return possible1,possible2 