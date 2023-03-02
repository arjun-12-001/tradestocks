import pickle as pk
from pathlib import Path 
import streamlit_authenticator as sauth 
import pandas as pd
import streamlit as st
import stonks 

st.title("Dashboard")

companies = stonks.comp(1)
option = st.selectbox(
    'How would you like to be contacted?',
    options = companies)

st.write('You selected:', option)
