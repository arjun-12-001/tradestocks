import pickle as pk
from pathlib import Path
import streamlit_authenticator as sauth

names = ["Arjun Ramesh","Harsha Joy"]
usernames = ["arjun_001","harsha_420"]
passwd = ["XXXX","XXXX"]

hashed_passwd = sauth.Hasher(passwd).generate()

file_path = Path(__file__).parent/"hashed_pw.pkl"
with open(file_path,"wb") as file:
    pk.dump(hashed_passwd,file)
