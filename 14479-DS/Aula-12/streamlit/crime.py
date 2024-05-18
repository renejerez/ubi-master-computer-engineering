import streamlit as st
import yfinance as yf
from datetime import datetime
import plotly.express as px
import pandas as pd


def load_data():
    df = pd.read_csv("https://query.data.world/s/6joi7hjgjmwifhl2clpldwm36xmvmx")
    df["REPORTDATETIME"] = pd.to_datetime(df["REPORTDATETIME"], infer_datetime_format=True)
    df["Day"] = df["REPORTDATETIME"].dt.day 
    df["Month"] = df["REPORTDATETIME"].dt.month
    df["Hour"] = df["REPORTDATETIME"].dt.hour
    return df

crime_df = load_data()


def display_map(df):
    fig = px.scatter_mapbox(df, lat="Y", lon="X", color="METHOD", zoom=10, height=300)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

display_map(crime_df)

st.map(crime_df,latitude='Y', longitude='X')