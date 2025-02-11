import streamlit as st 
from pathlib import Path
from frontend.kpi import ContentKPI, GenderKPI, AgeKPI, SubscriptionKPI
from frontend.graphs import ViewsTrend, SubscriptionChart, AgeChart, OperatingSystemChart


# device_kpi = DeviceKPI()
content_kpi = ContentKPI()
views_graph = ViewsTrend()

gender_kpi = GenderKPI()

age_chart = AgeChart()
age_kpi = AgeKPI()

subscription_kpi = SubscriptionKPI()
subscription_chart = SubscriptionChart()

operatingSystem_chart = OperatingSystemChart()

def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i min youtubekanal")
    # device_kpi.display_device_views()
    # device_kpi.display_device_summary()
    content_kpi.display_content()
    views_graph.display_plot()

    gender_kpi.display_content()

    age_kpi.display_content()
    age_chart.display_plot()

    subscription_kpi.display_content()
    subscription_chart.display_plot()

    operatingSystem_chart.display_plot()
    read_css()
    

def read_css():
    css_path = Path(__file__).parent/"frontend"/ "style.css"
    print(css_path)

    with open(css_path) as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True,
        )




if __name__ == "__main__":
    layout() 