from utils.query_database import QueryDatabase
import plotly.express as px
import streamlit as st 
import pandas as pd

class ViewsTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.views_per_date").df
       # print(self.df)

    def display_plot(self):
        fig = px.line(self.df, x="Datum", y="Visningar")
        st.markdown("## Antal visningar under senaste månaden")
        st.plotly_chart(fig)

# create more graphs here

class AgeChart:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.viewer_age_distribution;").df
        print(self.df)
    
    def display_plot(self):
        filtered_df = self.df[['Tittarnas ålder', 'Visningar (%)']] #plockar ut columner
        st.markdown("Visualisering")
        fig = px.bar(filtered_df, x='Tittarnas ålder', y='Visningar (%)')
        st.plotly_chart(fig) 


class SubscriptionChart:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.subscription_overview;").df
       # print(self.df)
    

    def display_plot(self):
        filtered_df = self.df.query("Prenumerationsstatus != 'Totalt' ") #filtering row with query
        st.markdown("### Procentuell visualisering")
        fig = px.pie(filtered_df, values='Visningar', names='Prenumerationsstatus', title='')
        st.plotly_chart(fig)
        #st.dataframe(self.df)

        