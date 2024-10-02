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
        fig = px.bar(filtered_df, 
                     x='Tittarnas ålder', 
                     y='Visningar (%)')
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


class OperatingSystemChart:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.operating_system;").df

    def display_plot(self):
        filtered_df = self.df[['Operativsystem', 'Visningar' ]]

        st.markdown(" ## Info kring operativsystem")
        st.markdown("Här visas information kring de olika operativsystemen som tittarna använt")

        selected_operatingSystem = st.selectbox(
            "välj operativsystem",
            filtered_df['Operativsystem'].unique()
        )

        fig = px.bar(
            filtered_df,
            x="Operativsystem", 
            y="Visningar", 
            title="Totala visningar per Operativsystem",
            labels={"Operativsystem": "Operativsystem", "Visningar": "Visningar"},
            color="Visningar"  
        )

        for data in fig.data:
            data.marker.opacity = [1 if os == selected_operatingSystem else 0.5 for os in filtered_df['Operativsystem']]

        st.plotly_chart(fig)
