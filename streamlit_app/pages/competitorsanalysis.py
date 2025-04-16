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

    scenarios = [
        "Idle - SwarNeTT", "Idle - Zello",
        "Heavy Load - SwarNeTT", "Heavy Load - Zello (Low)", "Heavy Load - Zello (High)"
    ]
    values = [0.1196, 0.0016, 0.041, 0.44, 1.69]
    colors = ['#F44336', '#2196F3', '#F44336', '#2196F3', '#2196F3']

    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(scenarios, values, color=colors)


    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.4f}', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5), textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)


    ax.set_ylabel("Data Usage (MB)", fontsize=14)
    ax.set_title("Data Usage Comparison: SwarNeTT vs Zello Walkie Talkie", fontsize=18, pad=20)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    st.pyplot(fig)

    st.write("""
    This chart compares *SwarNeTT* and *Zello Walkie Talkie* under both *idle* and *heavy load* conditions.

    - *SwarNeTT Idle*: 0.1196 MB  
    - *Zello Idle*: 0.0016 MB  
    - *SwarNeTT Heavy Load*: 0.041 MB  
    - *Zello Heavy Load* ranges from *0.44 MB* to *1.69 MB*, shown as two bars.

    """)