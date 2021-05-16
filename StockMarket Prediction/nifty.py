import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.title("Share Price analysis from Jan 2019 to May 2021:")
st.sidebar.title("Share Price analysis from Jan 2019 to May 2021:")
st.markdown("Share Price dashboard")
st.sidebar.markdown("Share Price dashboard")

st.sidebar.title("Please select a stock")
select = st.sidebar.selectbox('Share', ['TITAN.NS', 'BHARTIARTL.NS', 'HDFCLIFE.NS','ICICIBANK.NS','BAJFINANCE.NS','BAJAJ-AUTO.NS','CIPLA.NS','TATACONSUM.NS','TECHM.NS','TCS.NS','WIPRO.NS','TATASTEEL.NS','COALINDIA.NS'], key='1')

ticker_symbol = select

# Get data of this ticker
ticker_data = yf.Ticker(ticker_symbol)
# Get the historical prices for this ticker
ticker_df = ticker_data.history(period = '1d', start = '2019-01-01', end = '2021-05-16')

ticker_df = ticker_df.reset_index()

for i in ['Open', 'High', 'Close', 'Low']:
      ticker_df[i]  =  ticker_df[i].astype('float64')

avg_20 = ticker_df['Close'].rolling(window=20, min_periods=1).mean()
avg_50 = ticker_df['Close'].rolling(window=50, min_periods=1).mean()
avg_200 = ticker_df['Close'].rolling(window=200, min_periods=1).mean()
set1 = { 'x': ticker_df['Date'], 'open': ticker_df['Open'] ,'close': ticker_df['Close'], 'high': ticker_df['High'], 'low': ticker_df['Low'], 'type': 'candlestick',}
set2 = { 'x': ticker_df['Date'], 'y': avg_20, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'blue' },'name': 'MA 20 periods'}
set3 = { 'x': ticker_df['Date'], 'y': avg_50, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'yellow' },'name': 'MA 50 periods'}
set4 = { 'x': ticker_df['Date'], 'y': avg_200, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'black' },'name': 'MA 200 periods'}
data = [set1, set2, set3, set4]
fig = go.Figure(data=data)
st.plotly_chart(fig)
