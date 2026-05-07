from paths import PATHS, raw, processed, report, visual, query
import duckdb
import polars as pl 
import streamlit as st
import plotly.express as px

# Connect to db
conn = duckdb.connect(processed("crypto.db"))

# Query tables
market_df = conn.execute("SELECT * FROM market").pl()
ohlc_df = conn.execute("SELECT * FROM ohlc").pl()

# Dashboard
st.title("Crypto Leaderboard")
selected_coin = st.selectbox("Select coin", options=market_df['name'].to_list())
st.dataframe(market_df.select(["symbol", "name", "current_price", "market_cap", "price_range_24h"]))

selected_ohlc = ohlc_df.filter(pl.col("name") == selected_coin)
selected_ohlc = selected_ohlc.rename({"close": "Price", "ma_7d": "7D MA"})

fig = px.line(
    selected_ohlc, 
    x="timestamp", y=["Price", "7D MA"], 
    title=f"{selected_coin} 7D Moving Average"
)
st.plotly_chart(fig)