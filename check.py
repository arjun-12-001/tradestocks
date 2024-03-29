import streamlit as st 
import streamlit_authenticator as stauth 
from streamlit_authenticator import Authenticate
import yaml
from yaml.loader import SafeLoader

hashed_passwords = stauth.Hasher(['12345', '54321']).generate()
path = r"C:\Users\Arjun Ramesh\OneDrive\Desktop\portfolio\config.yaml"
with open(path) as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')