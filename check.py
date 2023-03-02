from turtle import pd
import streamlit as st
import plotly_express as px
import plotly.graph_objects as go
import pandas as pd
import stonks
import numpy as np
import json
import datetime
import requests 
from streamlit_lottie import st_lottie
import os
import yfinance as yf

st.set_page_config(layout="wide")

st.title("Portfolio Dashboard")

try:
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)
except:
    pass

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_i2eyukor.json")

path = os.path.abspath("lottiefiles/animate.json")
lottie_coding = load_lottiefile(path)

st_lottie(lottie_hello,key="hello",height=400,width=400)
# ----------------------------------------------------------------------------
with st.expander("Description"):
    st.markdown(""" 
    -This Dahboard allows you to selct a necessary stock you wish to proceed to buy or sell and 
    alalytics are done necessarily
""")

def run_col1():
    pass
def run_col2():
    pass
def run_col3():
    pass

with st.expander("Information Box"):
    col1,col2,col3 = st.columns(3)
    with col1:
        b1 = st.button("Total Invested Amount")
        run_col1()
    with col2:
        b2 = st.button("Number of Investments")
        run_col2()
    with col3:
        b3 = st.button("Return of Investments")
        run_col3()

st.sidebar.subheader("Select Company")
companies = stonks.comp(1)
option = st.sidebar.selectbox('', options = companies)
#comp name = option , symbol = val
val1 = stonks.comp(3,option)
symbol = str(val1)+".NS"

graph = st.sidebar.button("Launch "+option+" Graph")

colum1,colum2 = st.columns(2)
with colum1:
    if val1 is not None:
        data = yf.download(symbol)
        st.markdown("stock price of "+option)
        st.write(data.tail(10))    

# def datechange(d1,d2):


with colum2:
    if graph:
        d1 = st.date_input("Start date",datetime.date(2012, 7, 6))
        d1 = np.datetime64(d1)
        d2 = st.date_input("End date",datetime.date(2020, 7, 6))
        d2 = np.datetime64(d2)
        st.markdown("Chart of "+option)
        opn_cls=data[['Open','Close']]
        opn_cls.reset_index(inplace=True)
        opn_cls = opn_cls[opn_cls['Date']>d1]
        opn_cls = opn_cls[opn_cls['Date']<d2]
        
        opn_cls.set_index('Date',inplace=True)
        print(opn_cls)
        # opn_cls['Date'].astype(datetime)
        st.line_chart(opn_cls)  
        # if d1!= datetime.date(2012, 7, 6) or d2!=datetime.date(2020, 7, 6):
        #     datechange(d1,d2)
        

# try:
#     num_vals = list(data.select_dtypes(['int','float']).columns)
#     fraud = data[['trans_date_trans_time','merchant','category','gender','city','city_pop']]
#     st.write(fraud.head(100))
# except Exception as e:
#     print(e)
#     st.write("please upload file !")

# try:
#     st.markdown("## Here we have geographic representation of fraud transaction in US at 2020 ")
#     loc = data[['lat','lon']]
#     st.map(loc)
#     st.markdown("""- As we can see majority of fraud transactions are happening in major metropolitan areas
#     where people have more access to technology services and advancement in it """)
# except:
#     st.write('geographical locations based on fraudulence is unable to load !')


# chart_select = st.sidebar.selectbox(
#     label = 'select the chart type',
#     options=['Scatterplots','Bar Chart','Line-plot']
# )
# if chart_select == 'Line-plot':
#     try:
#         st.markdown("## All fraud transactions losses identified the last 6 months of 2020 ")
#         dates = pd.read_csv('recent.csv')
#         dates = dates.rename(columns={'date':'index'}).set_index('index')
#         st.line_chart(dates.head(6))
#     except:
#         pass


# if chart_select == 'Scatterplots':
#     st.sidebar.subheader("Scatterplots Settings")
#     try:
#         x_val = st.sidebar.selectbox('X axis', options=num_vals)
#         y_val = st.sidebar.selectbox('Y axis', options=num_vals)
#         plot = px.scatter(data_frame=data, x=x_val, y=y_val)
#         st.plotly_chart(plot)
#     except Exception as e:
#         print(e)

# if chart_select == 'Bar Chart':
#     st.markdown("### Bar Chart of most fraud transacted cities in US")
#     priority = pd.read_csv('staterank.csv')
#     priority = priority.head(6)
#     bar_chart = alt.Chart(priority).mark_bar().encode(
#         y = 'fraud frequency',
#         x = 'state',
#     )
#     st.altair_chart(bar_chart, use_container_width=True)

# if chart_select == 'Choropleth Map':
#     st.sidebar.subheader("Choropleth Map Settings")
#     try:
#         upload = st.sidebar.file_uploader(label="Upload your CSV or excel Mapping data(Max - 200MB)",
#                         type=['csv','xlsx'])
#         data_map = pd.read_csv(upload)
#         print(data_map.head)
#         # mapping function
#         data = dict(type = 'choropleth',
#             locations = data_map['short'],
#             z = data_map['fraud frequency'].astype(float),
#             locationmode = 'USA-states',
#             colorscale = 'Reds',
#             colorbar = {'title' : 'Fraudulent transaction frequency'},
#             text = data_map['Text'])

#         layout = dict(
#             title = '2020 credit fraud in USA',
#             geo = dict(scope = 'usa',
#                showlakes = True,
#                lakecolor = 'rgb(85,173,240)')
# )
#         choromap = go.Figure(data = [data], layout = layout)
#         choromap.show()     
#     except:
#         st.write('There seems to be an error loading map!')

# df = [['female',54],['male',46]]
#     # df = pd.DataFrame(df, columns=['gender','percentage'])
#     # fig = px.pie(df, values='percentage', names='gender', title='gender and victims')
#     # fig.show()
# st.markdown(' -Here we can see that women are subjected to higher fraud ')
# labels = 'Female','male'
# sizes = [54,46]
# explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# st.pyplot(fig1)

st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    # renderer="svg", # canvas
    height=720,
    width=720,
    key=None,
)
