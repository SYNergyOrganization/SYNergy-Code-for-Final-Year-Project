import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from data import *
import pandas as pd

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

    st.write("""
        During testing, it was discovered that infrastructure, such as concrete walls, affects the performance of SwarNeTT.
    """)

    # *Wi-Fi Direct & System Performance Analysis*
    st.subheader("Wi-Fi Direct & System Performance Analysis")
    st.write("This section visualizes packet transmission, TCP errors, throughput from PCAPdroid and analyzed by WireShark. Energy Used was determined using Android Studio.")

    # Packet Transmission Graph 
    packetsTransmittedInitialResults_df = pd.read_csv('data/packetsTransmittedInitialResults.csv')

    time_span = packetsTransmittedInitialResults_df['Interval start']
    packets_per_second = packetsTransmittedInitialResults_df['All Packets']

    st.subheader("Packet Transmission Over Time")

    fig, ax = plt.subplots(figsize=(14, 5))
    ax.plot(time_span, packets_per_second, marker='o', linestyle='-', color='b', label='Packets per Second')
    ax.set_xlabel('Interval')
    ax.set_ylabel('Packets per Second')
    ax.set_title('Wi-Fi Direct Packet Transmission')
    ax.legend()
    ax.grid()
    ax.set_xticks(time_span[::25]) 
    plt.xticks(rotation=45)         
    ax.set_xlim(min(time_span), max(time_span))
    st.pyplot(fig)

    # TCP Errors Graph
    tcpErrorInitialResults_df = pd.read_csv('data/tcpErrorInitialResults.csv')

    time_span = tcpErrorInitialResults_df['Interval start']
    tcp_errors = tcpErrorInitialResults_df['TCP Errors']

    st.subheader("TCP Errors Over Time")
    fig, ax = plt.subplots()
    ax.bar(time_span, tcp_errors, color='r', label='TCP Errors')
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Number of TCP Errors')
    ax.set_title('Wi-Fi Direct TCP Errors')
    ax.legend()
    ax.set_xticks(time_span[::25])  
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Throughput over time
    st.subheader("Throughput Over Time")
    ThroughputErrorInitialResults_df = pd.read_csv("data/throughput_for_inital.csv")

    fig, ax = plt.subplots(figsize=(14, 5))
    ax.plot(
        ThroughputErrorInitialResults_df["Interval start"],
        ThroughputErrorInitialResults_df["Throughput"],
        color="mediumblue",
        linewidth=1.5
    )
    ax.set_title("Network Throughput Over Time", fontsize=16)
    ax.set_xlabel("Interval Start")
    ax.set_ylabel("Throughput (Bytes/sec)")
    ax.grid(True, linestyle="--", alpha=0.5)
    st.pyplot(fig)

    # Power Consumption Graph
    st.subheader("Energy Used by Component")
    power_components = ["Display", "CPU Little", "CPU Big", "WLAN", "Sensor Core", "Memory", "CPU Mid", "UFS (Disk)", "Cellular", "GPU", "Camera", "GPS"]
    avg_power_mW = [414.76, 78.02, 50, 48.6, 27.19, 26.89, 20.96, 20.7, 19.16, 5.88, 1.33, 0]

    fig, ax = plt.subplots()
    ax.barh(power_components, avg_power_mW, color='purple')
    ax.set_xlabel('Power Consumption (mW)')
    ax.set_title('Average Power Consumption of System Components')
    st.pyplot(fig)

    st.success("Initial Results Complete!")




