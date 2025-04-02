import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def initialresults_page():
    st.markdown("<h1 style='font-size: 50px; color:#FF5733;'>Initial Results</h1>", unsafe_allow_html=True)
    
    # **Distance Coverage Graph**
    st.subheader("Distance Coverage by Environment")
    st.write("""
        This bar graph represents the distance coverage of SwarNeTT in different environments. 
        The graph shows the distance each environment can cover with varying levels of infrastructure.
    """)

    environments = ["Low Infrastructure & Forestry", "Medium Infrastructure & Forestry", "Heavy Infrastructure"]
    distances = [191, 160, 62]

    fig, ax = plt.subplots(figsize=(10, 6))  
    ax.bar(environments, distances, color=['#4CAF50', '#FF9800', '#F44336'])
    plt.xticks(rotation=45, ha="right", fontsize=14)
    ax.set_ylabel("Distance (m)", fontsize=14)
    ax.set_xlabel("Environment Type", fontsize=14)
    ax.set_title("Distance vs Environment", fontsize=18)
    plt.tight_layout()
    st.pyplot(fig)

