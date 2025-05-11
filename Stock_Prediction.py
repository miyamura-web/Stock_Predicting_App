import streamlit as st 
from pages.utils.model_train import get_data, get_rolling_mean, get_differencing_order, scaling, evaluate_model, get_forecast, inverse_scaling
import pandas as pd
from pages.utils.plotly_figure import plotly_table, Moving_average_forecast

st.set_page_config(

    page_title = "Stock Prdeiction",
    page_icon = "charts_with_downwards_trend",
    layout = 'wide',
)

 # st.title("Stock Prediction")



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

    <div class="fake-header"> 📊 Stock Prediction </div>
    """,
    unsafe_allow_html=True
)









col1, col2, col3 = st.columns(3)

with col1:
    ticker = st.text_input('Stock Ticker', 'TSLA')

rmse = 0

st.subheader('Predicting Next 30 days Stock Price for:' +ticker)

close_price = get_data(ticker)
rolling_price = get_rolling_mean(close_price)

differencing_order = get_differencing_order(rolling_price)
scaled_data, scaler = scaling(rolling_price)
rmse = evaluate_model(scaled_data, differencing_order)

st.write("**Model RMSE Score:**",rmse)

forecast = get_forecast(scaled_data, differencing_order)

forecast['Close'] = inverse_scaling(scaler, forecast['Close'])
st.write('##### Forecast Data (Next 30 days)')
fig_tail = plotly_table(forecast.sort_index(ascending = True).round(3))
fig_tail.update_layout(height = 220)
st.plotly_chart(fig_tail, use_container_width= True)

# For combined plot (past + future)
# forecast = pd.concat((rolling_price, forecast))
# st.plotly_chart(Moving_average_forecast(forecast.iloc[150:]), use_container_width=True)

# Only plot future forecasted prices
st.plotly_chart(Moving_average_forecast(forecast), use_container_width=True)




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

