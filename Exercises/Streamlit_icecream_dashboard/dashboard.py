import streamlit as st
import pandas as pd
from pathlib import Path

def read_data():
    data_path = (__file__).parent[2] / "Data"
    df = pd.read_csv(data_path / "IceCreamData.csv", index_col = 0, parse_dates=[0])
    df.index = df.index.revenue
    return df

def layout():
    df = read_data()
    st.markdown ("# ")