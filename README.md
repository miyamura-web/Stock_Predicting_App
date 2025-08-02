# Stock_Predicting_App

## 📈 Stock Analysis & Forecasting Hub

This is a personal project I built from scratch using **Python** and **Streamlit**, designed to help users analyze stock performance, explore technical indicators, and forecast future stock prices based on historical trends. The app combines real-time data analysis with predictive modeling to support smarter, data-driven investment decisions.

![Screenshot 2025-05-11 164733](https://github.com/user-attachments/assets/108d2363-e6f7-4a98-a053-63c10516c5e3)


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## 📘 About the App :
This application is organized into three main pages to provide a seamless stock research experience:

### 🏠 Home Page
A welcoming entry point to the app that introduces its features and guides users on how to navigate through the platform.

### 📊 Stock Analysis Page
 - Enter your favorite stock ticker (e.g., TSLA, AAPL)
   - View company details like sector, website, and number of employees
   - Analyze key financial metrics including Market Cap, P/E Ratio, EPS, ROE, and more
   - Access historical stock price data with flexible date filters
   - Visualize trends using interactive line and candlestick charts
   - Add technical indicators such as RSI, MACD, and Moving Averages

### 🔮 Stock Prediction Page
- Generate 30-day closing price forecasts using a custom time-series pipeline
   - View RMSE model evaluation scores
   - Understand future stock trends through interactive forecast charts

![Screenshot 2025-05-11 165101](https://github.com/user-attachments/assets/e7499176-bac5-43de-b9ae-653a0b7d3796)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## How to use :
In the Ticker section, simply type your favorite stock ticker symbol (e.g., TSLA, AAPL, MSFT) and press Enter. The app will display all relevant stock information, including company details, key financial metrics, historical data, and interactive charts.

![Screenshot 2025-05-11 164918](https://github.com/user-attachments/assets/462c3443-c0a8-4c01-84c4-e1670c6fcb95)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## 🛠️ Tech Stack

- **Library**: Streamlit, Scikit-learn, Statsmodels, Plotly, Numpy, Pandas 
- **Data Sources**: Yahoo Finance (`yfinance`)
- **Visualization**: Plotly
- **Modeling**: Custom forecasting pipeline (ARIMA-style logic)

---


## 📊 Graphs & Visualizations

This app includes a range of interactive and insightful charts to enhance stock analysis and prediction:

#### 📉 In the Stock Analysis Page:
- **Line Charts** – Track historical closing prices over time.
- **Candlestick Charts** – Visualize price movement with open, high, low, and close.
- **RSI (Relative Strength Index)** – Identify overbought or oversold conditions.
- **MACD (Moving Average Convergence Divergence)** – Analyze momentum and trend strength.
- **Moving Averages** – Smooth out price data to spot trends.

![Screenshot 2025-05-11 164852](https://github.com/user-attachments/assets/df0b0fd7-3d05-47e1-9152-78abae65dce2)

--

#### 🔮 In the Stock Prediction Page:
- **Forecast Line Chart** – Displays predicted closing prices for the next 30 days.
- **Forecast Table (Interactive)** – View forecasted prices with precision and scrollability.
- **Model Evaluation Plot (optional)** – Understand model performance using RMSE.

Each graph is built using **Plotly** for responsiveness and interactivity, allowing zoom, hover, and export options.

![Screenshot 2025-05-11 172944](https://github.com/user-attachments/assets/2029d193-2d9d-4a10-b200-f1f94809e529)


---



## 📁 Folder Structure
- Home.py                     
- pages directory
   - Stock_Analysis.py         
   - Stock_Prediction.py      
   - utils
      - model_train.py         
      - plotly_figure.py       
      - __init__
       
- app.png                    
- SOURCES.txt
- README.md



---


## ⚠️ Disclaimer

*This project is built for educational and demonstration purposes only. The stock predictions and analysis provided by the app are based on historical data and do not constitute financial advice. Always conduct your own research before making investment decisions.*

##### 💡 Would appreciate your help in deploying this app as a public URL or any cloud hosting service. Feel free to fork the repo or contribute with suggestions!


