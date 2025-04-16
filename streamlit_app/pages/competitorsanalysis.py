import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

def competitorsanalysis_page():

    systems = ["SwarNeTT", "goTenna"]
    distances = [62, 8845]  


    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(systems, distances, color=['#F44336', '#2196F3'])


    ax.set_ylabel("Distance (m)", fontsize=14)
    ax.set_title("Distance Coverage in Heavy Infrastructure", fontsize=18)
    plt.tight_layout()

   
    st.pyplot(fig)


    st.write("""
    This bar chart compares the distance coverage in heavy infrastructure environments between SwarNeTT and goTenna.
    
    - **SwarNeTT** covers up to **62 metres**
    - **goTenna** covers up to **8845 metres**

    The chart shows the significant difference in range performance under heavy infrastructure conditions.
    """)

