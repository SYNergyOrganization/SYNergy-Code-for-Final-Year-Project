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

    # *Wi-Fi Direct & System Performance Analysis*
    st.subheader("Wi-Fi Direct & System Performance Analysis")
    st.write("This section visualizes packet transmission, TCP errors, packet loss, throughput, and system power consumption from a Wireshark capture and system profiler.")

    # Data extracted from Wireshark I/O Graph and Sequence Number Graph
    time_span = [0, 10, 50, 100, 150, 200, 250, 282]  # Actual timestamps from I/O graph
    packets_per_second = [5, 20, 30, 10, 5, 15, 25, 10]  # Packet transmission rates from I/O graph
    tcp_errors = [0, 2, 5, 3, 1, 4, 6, 2]  # TCP Errors extracted from graph
    packet_loss = [1, 3, 7, 4, 2, 5, 9, 3]  # Packet loss from sequence analysis
    throughput = [3500, 4000, 4500, 3000, 2500, 3200, 3700, 3300]  # Throughput calculated from PCAP analysis


