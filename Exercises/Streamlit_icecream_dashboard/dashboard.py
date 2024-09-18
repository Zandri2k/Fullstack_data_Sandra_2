import streamlit as st
import pandas as pd
from pathlib import Path

#regression prblm kolla förra kursen

#Reading the data
def read_data():
    data_path = Path(__file__).parents[2] / "Data"
    df = pd.read_csv(data_path / "IceCreamData.csv", index_col = 0, parse_dates=[0])
    
    return df
 
#Where tha data displays
def layout():
    df = read_data()
    st.markdown ("# Ice Cream Revenue Prediction")
    st.dataframe(df,height= 400)    

if __name__ == '__main__':
    layout()