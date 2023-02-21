import pickle as pk
from pathlib import Path 
import streamlit_authenticator as sauth 
import pandas as pd
import streamlit as st
import stonks 

companies = stonks.comp(1)
option = st.selectbox(
    'How would you like to be contacted?',
    options = companies)

st.write('You selected:', option)




# names = ["Arjun Ramesh","Harsha Joy"]
# usernames = ["arjun_001","harsha_420"]

# file_path = Path(__file__).parent/"hashed_pw.pkl"
# with open(file_path,"rb") as file:
#     hashed_pwd = pk.load(file)

# auth = (names,usernames,hashed_pwd,)