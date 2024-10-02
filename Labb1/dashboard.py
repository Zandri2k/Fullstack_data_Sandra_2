import streamlit as st 
from frontend.kpi import ContentKPI, GenderKPI, AgeKPI, SubscriptionKPI
from frontend.graphs import ViewsTrend


# device_kpi = DeviceKPI()
content_kpi = ContentKPI()
views_graph = ViewsTrend()
gender_kpi = GenderKPI()
age_kpi = AgeKPI()
subscription_kpi = SubscriptionKPI()

def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i min youtubekanal")
    # device_kpi.display_device_views()
    # device_kpi.display_device_summary()
    content_kpi.display_content()
    views_graph.display_plot()
    gender_kpi.display_content()
    age_kpi.display_content()
    subscription_kpi.display_content()




if __name__ == "__main__":
    layout()