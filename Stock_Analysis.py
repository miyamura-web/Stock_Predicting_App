import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import datetime
import ta
from pages.utils.plotly_figure import plotly_table
from pages.utils.plotly_figure import close_chart
from pages.utils.plotly_figure import candlestick
from pages.utils.plotly_figure import RSI
from pages.utils.plotly_figure import Moving_average
from pages.utils.plotly_figure import MACD

# from pages.utils.plotly_figure import filter_data



# Setting page config
st.set_page_config(
    page_title="Trading App",
    page_icon = "charts_with_downwards_trend",
    layout="wide"
)

# st.title("Stock Analysis 💹 ")


st.markdown(
    """
    <style>
        /* Main content */
        .block-container {
            background-color: #fff8dc;
            color: black;
            padding: 2rem;
        }

        /* Fake header to simulate top bar with your name */
        .fake-header {
            margin-top: 3.5rem;  /* Push down below Streamlit nav bar */
            background-color: #1e3a5f;  /* Dark blue */
            padding: 15px 25px;
            color: white;
            font-size: 24px;
            font-weight: bold;
            border-bottom: 3px solid #FFD700;  /* Gold underline */
            z-index: 10;
            position: relative;
        }

        /* Optional: Style the real Streamlit top bar */
        .stAppHeader {
            background-color: #008080 !important;
        }
    </style>

    <div class="fake-header"> 💹 Stock Analysis </div>
    """,
    unsafe_allow_html=True
)







col1, col2, col3 = st.columns(3)

today = datetime.date.today()

with col1:
    ticker = st.text_input("Stock Sticker", "TSLA")
with col2:
    start_date = st.date_input("Choose start date", datetime.date(today.year -1, today.month, today.day))
with col3:
    end_date = st.date_input("Choose end date", datetime.date(today.year, today.month, today.day))


st.subheader(ticker)

stock = yf.Ticker(ticker)    # Store the stock data

st.write(stock.info['longBusinessSummary'])
st.write("**Sector :**",stock.info['sector'])
st.write("**Full Time Employess :**",stock.info['fullTimeEmployees'])
st.write("**Website :**",stock.info['website'])


st.write('##### Key Financial Metrics ')

col1, col2 = st.columns(2)

with col1:
   df = pd.DataFrame(index = ['Market Cap', 'Beta','EPS', 'PE Ratio'])
   df['Metrics'] = [
    stock.info.get("marketCap", None),
    stock.info.get("beta", None),
    stock.info.get("trailingEps", None),
    stock.info.get("trailingPe", None)]
   fig_df = plotly_table(df)
   st.plotly_chart(fig_df, use_container_width=True)

with col2:
    df = pd.DataFrame(index = ['Quick Ratio', 'Revenue per share','Profit Margins', 'Debt to Equity', 'Return on Equity'])
    df['Ratios'] = [stock.info["quickRatio"],stock.info["revenuePerShare"],stock.info["profitMargins"],stock.info["debtToEquity"],stock.info["returnOnEquity"]]
    fig_df = plotly_table(df)
    st.plotly_chart(fig_df, use_container_width=True)



data = yf.download(ticker, start = start_date, end = end_date)  # Downloading the data
# Flatten columns if multi-indexed
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)


col1, col2, col3 = st.columns(3)

close_price = float(data['Close'].iloc[-1])  # explicitly convert
daily_change = float(data['Close'].iloc[-1] - data['Close'].iloc[-2])
col1.metric("Daily Change", f"{round(close_price, 2)}", f"{round(daily_change, 2)}")

last_10_df = data.tail(10).sort_index(ascending=False).round(3)
fig_df = plotly_table(last_10_df)

st.write('##### Historical Data (Last 10 Days)')
st.plotly_chart(fig_df, use_container_width=True)

# For the buttons
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col10, col11, col12 = st.columns([1,1,1,1,1,1,1,1,1,1,1,1,1])

num_period = ''
with col1:
    if st.button('5D'):
        num_period = '5d'
with col2:
    if st.button('1M'):
        num_period = '1mo'
with col3:
    if st.button('6M'):
        num_period = '6mo'    
with col4:
    if st.button('YTD'):
        num_period = 'ytd'
with col5:
    if st.button('1Y'):
        num_period = '1y'
with col6:
    if st.button('5Y'):
        num_period = '5y'   
with col7:
    if st.button('10Y'):
        num_period = '10Y' 
with col8:
    if st.button('MAX'):
        num_period = 'MAX'



# For the Graphs Buttons
col1, col2, col3 = st.columns([1,1,4])
with col1:
    chart_type = st.selectbox('',('Candle','Line'))
with col2:
    if chart_type == 'Candle':
        indicators = st.selectbox('', ('RSI','MACD'))
    else:
        indicators = st.selectbox('',('RSI','Moving Average','MACD'))



# For the Graphs
ticker = yf.Ticker(ticker)
new_df = ticker.history(period = 'max')
data1 = ticker.history(period = 'max')
if num_period == '':

    if chart_type == 'Candle' and indicators =='RSI':
        st.plotly_chart(candlestick(data1, '1y'), use_container_width=True)
        st.plotly_chart(RSI(data1, '1y'), use_container_width=True)


    if chart_type == 'Candle' and indicators =='MACD':
        st.plotly_chart(candlestick(data1, '1y'), use_container_width=True)
        st.plotly_chart(MACD(data1, '1y'), use_container_width=True)

    
    if chart_type == 'Line' and indicators =='RSI':
        st.plotly_chart(close_chart(data1, '1y'), use_container_width=True)
        st.plotly_chart(RSI(data1, '1y'), use_container_width=True)


    if chart_type == 'Line' and indicators =='MACD':
        st.plotly_chart(close_chart(data1, '1y'), use_container_width=True)
        st.plotly_chart(MACD(data1, '1y'), use_container_width=True)


    if chart_type == 'Line' and indicators =='Moving Average':
        st.plotly_chart(Moving_average(data1, '1y'), use_container_width=True)

else:
    if chart_type == 'Candle' and indicators =='RSI':
        st.plotly_chart(candlestick(new_df, num_period), use_container_width=True)
        st.plotly_chart(RSI(data1, '1y'), use_container_width=True)


    if chart_type == 'Candle' and indicators =='MACD':
        st.plotly_chart(candlestick(new_df, num_period), use_container_width=True)
        st.plotly_chart(MACD(data1, '1y'), use_container_width=True)


    if chart_type == 'LIne' and indicators =='RSI':
        st.plotly_chart(close_chart(new_df, num_period), use_container_width=True)
        st.plotly_chart(RSI(data1, '1y'), use_container_width=True)


    if chart_type == 'Line' and indicators =='MACD':
        st.plotly_chart(close_chart(new_df, num_period), use_container_width=True)
        st.plotly_chart(MACD(data1, '1y'), use_container_width=True)

    if chart_type == 'Line' and indicators =='Moving Average':
        st.plotly_chart(Moving_average(data1, '1y'), use_container_width=True)


       