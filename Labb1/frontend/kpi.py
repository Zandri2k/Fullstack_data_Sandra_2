import streamlit as st
from utils.query_database import QueryDatabase

class ContentKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.content_view_time;").df

    def display_content(self):
        df = self._content
        st.markdown("## KPIer för videor")
        st.markdown("Nedan visas KPIer för totalt antal")

        kpis = {
            "videor": len(df),
            "visade timmar": df["Visningstid_timmar"].sum(),
            "prenumeranter": df["Prenumeranter"].sum(),
            "exponeringar": df["Exponeringar"].sum(),
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col: 
                st.metric(kpi, round(kpis[kpi]))
        st.dataframe(df)

# create more KPIs here
class DeviceKPI:
    pass 


class GenderKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.viewer_sex_distribution;")

    def display_content(self):
        df = self._content.df 

        st.markdown("## KPIer över köns och åldersfördelning")
        st.markdown("KPIn nedanför visar könsfördelningen över youtubekanalen")
        st.dataframe(df)


class AgeKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.viewer_age_distribution;")

    def display_content(self):
        df = self._content.df

        #st.markdown("## KPI över åldersfördelningen")
        st.markdown("KPIn nedanför visar åldersfördelningen över youtubekanalen")
        st.dataframe(df)
 

class SubscriptionKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.subscription_overview;")

    def display_content(self):
        df = self._content.df

        st.markdown("## Prenumerationsstatus")
        st.markdown("Här visualiseras data över youtubkanalens prenumarationsstatus")
        st.dataframe(df)




       
