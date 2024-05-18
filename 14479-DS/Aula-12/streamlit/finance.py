import streamlit as st
import yfinance as yf
from datetime import datetime

def finance(ticker):
    #get data on this ticker
    tickerData = yf.Ticker(ticker)

    #get the historical prices for this ticker
    now = datetime.today().strftime('%Y-%m-%d')

    ticker_DF = tickerData.history(period='1d', start='2010-5-31', end=now)
    
    return ticker_DF

ticker_DF = finance('GOOGL')

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")

st.line_chart(ticker_DF["Close"])
st.line_chart(ticker_DF["Volume"])