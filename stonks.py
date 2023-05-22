import pandas as pd

def comp(val=0,compy_name ="NULL"):
  sym_names = {}
  if val == 1 and compy_name == "NULL":
    data = pd.read_csv("names_new.csv")
    comp_names = data["Company Name"]
    return comp_names

  elif val == 0 and compy_name == "NULL":    
    data = pd.read_csv("names_new.csv")
    symbols = data["Symbol"]
    comp_names = data["Company Name"]
    count = 0

    for comp_name in comp_names:
      sym_names[comp_name] = symbols[count]
      count = count + 1 
    
    possible1 = []
    possible2 = []
    string = comp_name.lower()
    substr = data["Compnay Name"].tolist()
    for comp in substr:
      if comp.lower().startswith(string):
        possible1.append(sym_names[comp])
        possible2.append(comp)
    return possible1,possible2 
  
  elif val==3 and compy_name != "NULL":
    data = pd.read_csv("names_new.csv")
    symbols = data["Symbol"]
    comp_names = data["Company Name"]
    count = 0

    for comp_name in comp_names:
      sym_names[comp_name] = symbols[count]
      count = count + 1 
    return sym_names[compy_name]

  elif val==4 and compy_name != "NULL":
    names = []
    simps = []
    sym_names = {}
    data = pd.read_csv("names_new.csv")
    symbols = data["Symbol"]
    comp_names = data["Company Name"].tolist()
   
    count = 0
    for comp_name in comp_names:
      sym_names[comp_name] = symbols[count]
      count = count + 1 
    
    for comp in comp_names:
      if comp.lower().startswith(compy_name):
        names.append(comp)
        simps.append(sym_names[comp])
    return names,simps    