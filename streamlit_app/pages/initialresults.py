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

    st.write("""
        During testing, it was discovered that infrastructure, such as concrete walls, affects the performance of SwarNeTT.
    """)

    # *Wi-Fi Direct & System Performance Analysis*
    st.subheader("Wi-Fi Direct & System Performance Analysis")
    st.write("This section visualizes packet transmission, TCP errors, packet loss, throughput from PCAPdroid and analyzed by WireShark. Energy Used was determined using Android Studio.")

    # Data extracted from Wireshark I/O Graph and Sequence Number Graph
    time_span = [0, 10, 50, 100, 150, 200, 250, 282]  # Actual timestamps from I/O graph
    packets_per_second = [5, 20, 30, 10, 5, 15, 25, 10]  # Packet transmission rates from I/O graph
    tcp_errors = [0, 2, 5, 3, 1, 4, 6, 2]  # TCP Errors extracted from graph
    packet_loss = [1, 3, 7, 4, 2, 5, 9, 3]  # Packet loss from sequence analysis
    throughput = [3500, 4000, 4500, 3000, 2500, 3200, 3700, 3300]  # Throughput calculated from PCAP analysis

    # Packet Transmission Graph
    st.subheader("Packet Transmission Over Time")
    fig, ax = plt.subplots()
    ax.plot(time_span, packets_per_second, marker='o', linestyle='-', color='b', label='Packets per Second')
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Packets per Second')
    ax.set_title('Wi-Fi Direct Packet Transmission')
    ax.legend()
    ax.grid()
    st.pyplot(fig)

    # TCP Errors Graph
    st.subheader("TCP Errors Over Time")
    fig, ax = plt.subplots()
    ax.bar(time_span, tcp_errors, color='r', label='TCP Errors')
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Number of TCP Errors')
    ax.set_title('Wi-Fi Direct TCP Errors')
    ax.legend()
    #ax.grid()
    st.pyplot(fig)

    # Packet Loss Graph
    st.subheader("Packet Loss Over Time")
    fig, ax = plt.subplots()
    ax.bar(time_span, packet_loss, color='orange', label='Packet Loss')
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Number of Lost Packets')
    ax.set_title('Packet Loss Events Over Time')
    ax.legend()
    ax.grid()
    st.pyplot(fig)

    # Throughput Graph
    st.subheader("Throughput Over Time")
    fig, ax = plt.subplots()
    ax.plot(time_span, throughput, marker='o', linestyle='-', color='green', label='Throughput (bps)')
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Throughput (bps)')
    ax.set_title('Network Throughput Over Time')
    ax.legend()
    ax.grid()
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




