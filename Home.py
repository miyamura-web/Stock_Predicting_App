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
st.title("Welcome to the Stock Prediction Dashboard 📈")
st.markdown(
    "We provide the greatest platform to collect all information before making informed stock investments. "
    "Our tools offer insights into stock trends, predictions, and real-time data analysis."
)




st.image("app.png", caption="Stock Prediction App", use_container_width=True)



st.markdown("## We provide the following services:")

st.markdown("#### :one: Stock Information")
st.write("Through this page, you can see all the information about stock.")

st.markdown("#### :two: Stock Prediction")
st.write("You can explore predicted closing prices for the next 30 days based on historical stock data and advanced forecasting models. Use this tool to gain valuable insights into market trends and make informed investment decisions.")

#st.markdown('#### :three: CAPM Return')
#st.write("Discover how the Capital Asset Pricing Model (CAPM) calculates the expected return of different stock assets based on their risk and market performance.")

# st.markdown('#### :four: CAPM Beta')
# st.write("Calculates Beta and Expected Return for Individual Stocks.")




st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 10px;
            right: 10px;
            font-size: 12px;
            color: grey;
        }
    </style>
    <div class="footer">
        © 2025 Trading Guide App - All Rights Reserved. | Built with Streamlit
    </div>
    """, 
    unsafe_allow_html=True
)
