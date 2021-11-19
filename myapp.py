import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Stock Price Chart Application
Shown are the stock **Closing Price** and **Volume** of Google! """
)
#Define the ticker symbol
tickerSybmol = 'GOOGL'

#get the data on this ticker
tickerData = yf.Ticker(tickerSybmol)

tickerDf = tickerData.history(period = '1d',start ='2010-5-31',end ='2022-5-31')
st.write(""" ## Closing Price""")
st.line_chart(tickerDf["Close"])
st.write(""" ## Volume Price""")

st.line_chart(tickerDf["Volume"])



