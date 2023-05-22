import streamlit as st
import altair as alt
import pandas as pd
import plotly.express as px
import database as db
import yfinance as yf
import stonks

def color_negative_red(val):
    try:
        if val.startswith("-"):
            return 'color: red'
        elif val.startswith("+"):
            return 'color: green'
    except:
        pass

st.header("Personal Portfolio page 📈")
# Create some sample data for the pie chart
st.sidebar.subheader("Select Company")
companies = stonks.comp(1)
option = st.sidebar.selectbox('', options = companies)
capital,invested = db.capital()
cap_perc=float(capital/(capital+invested))*100
inv_perc=float(invested/(capital+invested))*100

data = pd.DataFrame({
    'Category': ['Capital', 'Invested'],
    'Value': [cap_perc, inv_perc]
})

# Create the pie chart with interactivity
chart = alt.Chart(data).mark_bar().encode(
    alt.X('Value', title='Value'),
    alt.Y('Category', title='Category'),
    color='Category',
    tooltip=['Category', 'Value']
).interactive()

st.altair_chart(chart, use_container_width=True)

st.subheader("Holdings")
with st.expander('details'):
    values = db.holdings()
    comp=values[0]
    qty=values[1]
    price=values[2]
    ticker = yf.Ticker(comp)
    historical_data = ticker.history(period="2d", interval="1h")
    previous_close_price = historical_data.iloc[-1]["Close"]
    gain = ((previous_close_price-price)/price)*100
    if gain>0:
        gain = "+"+str(gain)
    else:
        gain = "-"+str(gain)
    data = {'Company': [comp], 'Quantity': [qty], 'Purchase Price': [price],'Last Close Price':previous_close_price,'P & L':[gain]}
    df = pd.DataFrame(data,index=[0])
    styled_df = df.style.applymap(color_negative_red)
    st.table(styled_df)
# Button to sell off with red color
b1 = st.button('Sell Off', help='Click to sell off')
if b1:
    all = st.button('Sell All')
    st.write('OR')
    quantity = st.text_input("enter quantity to sell: ")
        
    confirm=False
    if all:
        vall = "all"
    else:        
        val = "some"
    confirm=True    
    if confirm == True:
        st.write("Are you sure?")
        if st.button("Confirm"):
            if vall == "all":
                db.sell(qty,comp)
                db.profits(previous_close_price,qty,val)
                st.write("Confirmed!")
            elif vall == "some":
                st.write("some works")
                db.sell(quantity,comp,val)
                db.profits(previous_close_price,quantity,comp)

st.subheader("Buy Equity")
val1 = stonks.comp(3,option)
symbol = str(val1)+".NS"
tick = symbol.lower()
data = yf.Ticker(tick)
val = data.history(period='1d',interval="1h")
last_price = val.iloc[-1]["Close"]
d1 = {'Company Name':[option],"Last Traded Price":[last_price]}
d1 = pd.DataFrame(d1, index=[0])
st.table(d1)
values = st.text_input('enter the quantity to be purchased : ')
b2 = st.button('Buy', help='Click to buy')
if b2:
    st.write("B2 works")
    # if db.count_positions() != 0:
        # db.buy_new(tick,values,last_price)

# else:
#     st.warning("Already holding Position !")

# Display the chart in Streamlit


# fig = px.pie(data, values='Value', names='Category')

# # Display the chart in Streamlit
# st.plotly_chart(fig)

