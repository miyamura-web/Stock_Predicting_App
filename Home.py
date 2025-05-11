import streamlit as st

st.set_page_config(page_title="Trading App", page_icon = "charts_with_downwards_trend", layout="wide")

# Fix for header visibility
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

    <div class="fake-header">👤 Niladri's — Trading Guide App</div>
    """,
    unsafe_allow_html=True
)

# Now the rest of your app
st.title(" 📈 Welcome to The Stock Analysis and Forecasts Hub ")
st.markdown(
    "I’ve built this platform to help you gather everything you need before making informed stock investment decisions. " \
    "It brings together real-time data analysis, historical trends, and future price predictions—all in one place to support smarter, data-driven choices. " \
    "The platform leverages advanced algorithms and machine learning models to analyze stock performance, identifying patterns and forecasting future trends. " \
    "By combining historical data with real-time insights, it allows you to assess the market’s current state and make more accurate predictions about where it’s headed. " \
    "With this comprehensive tool, you can stay ahead of the curve, monitor market shifts, and ensure that your investment strategy is always based on reliable, up-to-date information. " \
    "This ensures you're equipped with the knowledge necessary to make strategic decisions, minimizing risk while maximizing potential returns.")




st.image("app.png", caption="Stock Prediction App", use_container_width=True)



st.markdown("### You'll get to know detailed insights about :")

st.markdown("#### :one: Stock Information")
st.write("Through this page, you'll get to know all essential information about a stock, including the company's profile with details like its sector, official website, and workforce size. " \
"It also covers key financial ratios such as market capitalization, beta, earnings per share, P/E ratio, return on equity, and debt-to-equity ratio. " \
"In addition, you can explore historical stock price data presented in both table and chart formats, along with interactive visualizations that help you analyze trends over various time periods using tools like candlestick and line charts combined with technical indicators such as RSI, MACD, and moving averages. ")

st.markdown("#### :two: Stock Prediction")
st.write("By utilizing advanced forecasting models on historical stock data, you can predict the closing prices for the next 30 days, offering valuable insights into future market trends. " \
"These predictions are generated using time series analysis and machine learning techniques, such as ARIMA, SARIMA, and deep learning models, which take into account various factors like historical price patterns, volume trends, and macroeconomic indicators. " \
"With this tool, you can observe fluctuations and trends in stock prices, helping you make well-informed decisions regarding your investments. Predicting the stock market with precision allows investors to assess risk, identify potential growth opportunities, and optimize their portfolios by anticipating price movements. " \
"By leveraging these advanced forecasting models, it’s possible to better understand market dynamics and position oneself for success in a competitive financial landscape.")

#st.markdown('#### :three: CAPM Return')
#st.write("Discover how the Capital Asset Pricing Model (CAPM) calculates the expected return of different stock assets based on their risk and market performance.")

# st.markdown('#### :four: CAPM Beta')
# st.write("Calculates Beta and Expected Return for Individual Stocks.")



# For Trade mark
import datetime

current_year = datetime.datetime.now().year

st.markdown(
    f"""
    <style>
        .footer {{
            position: none;
            bottom: 10px;
            right: 10px;
            font-size: 12px;
            color: grey;
        }}
    </style>
    <div class="footer">
        © {current_year} Trading Guide App - All Rights Reserved. | Built with Streamlit
    </div>
    """, 
    unsafe_allow_html=True
)
