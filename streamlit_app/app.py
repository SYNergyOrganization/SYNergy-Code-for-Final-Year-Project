import streamlit as st
from pages.home import homepage
from pages.competitors import competitors_page
from pages.initialresults import initialresults_page
from pages.finalresults import finalresults_page
from pages.competitorsanalysis import competitorsanalysis_page

# Sidebar navigation
st.sidebar.markdown("<h2 style='font-size: 24px;'>Navigation</h2>", unsafe_allow_html=True)
page = st.sidebar.radio("Go to", ("Home", "Competitors","Competitors Analysis", "Initial Results", "Final Results"), index=0)

# Page content
if page == "Home":
    homepage()
elif page == "Competitors":
    competitors_page()
elif page =="Competitors Analysis":
    competitorsanalysis_page()
elif page == "Initial Results":
    initialresults_page()
elif page == "Final Results":
    finalresults_page()
