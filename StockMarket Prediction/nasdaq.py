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
select = st.sidebar.selectbox('Share', ['GOOGL', 'AAPL', 'MSFT','AMZN','TSLA','BABA','JPM','JNJ','WMT','NVDA','PYPL','PFE'], key='1')

ticker_symbol = select

# Get data of this ticker
ticker_data = yf.Ticker(ticker_symbol)
# Get the historical prices for this ticker
ticker_df = ticker_data.history(period = '1d', start = '2019-01-01', end = '2021-05-16')

st.write("""Closing Price""")
st.line_chart(ticker_df.Close)
st.write("""Volume""")
st.line_chart(ticker_df.Volume)
# Check firms calls about this Stock
st.write("Firms opinions")
st.write(ticker_data.recommendations)
st.write("Company's earnings and revenue")
st.write(ticker_data.calendar)
st.write("Options expiry dates")
st.write(ticker_data.options)
