import streamlit as st
import matplotlib.pyplot as plt


def finalresults_page():
    st.markdown("<h1 style='font-size: 50px; color:#FF5733;'>Final Results</h1>", unsafe_allow_html=True)
    st.write("""
        These are the final results of the SwarNeTT system after further testing, with refined data and conclusions.
    """)

    # battery usage state at idle
    st.subheader("Battery Consumption while app is idling")
    st.write("This bar chart shows the average power usage (in mW) by each system component while SwarNeTT is idle.")

    labels_idle = [
        "CPU Big", "Display", "WLAN", "CPU Little", "Memory",
        "Sensor Core", "UFS (Disk)", "Cellular", "CPU Mid", "GPU", "Camera", "GPS"
    ]
    power_idle = [
        1218.32, 452.24, 236.89, 178.06, 44.42,
        27.28, 26.69, 19.09, 20.51, 4.03, 0.64, 0
    ]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(labels_idle, power_idle, color='skyblue')
    ax.set_xlabel('Power Consumption (mW)')
    ax.set_title('Idle: Average Power Consumption by Component')
    #ax.invert_yaxis()
    st.pyplot(fig)

    # battery usage state under load
    st.subheader("Battery Consumption while app is under load")
    st.write("This bar chart shows the average power usage (in mW) by each system component while SwarNeTT is actively being used.")

    labels_load = [
        "CPU Big", "Display", "WLAN", "CPU Little", "Memory",
        "Sensor Core", "UFS (Disk)", "Cellular", "CPU Mid", "GPU", "Camera", "GPS"
    ]
    power_load = [
        1202.04, 455.05, 231.36, 200.22, 58.7,
        28.19, 26.25, 18.19, 11.1, 7.15, 0.95, 0
    ]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(labels_load, power_load, color='salmon')
    ax.set_xlabel('Power Consumption (mW)')
    ax.set_title('Under Load: Average Power Consumption by Component')
    #ax.invert_yaxis()
    st.pyplot(fig)

    # TCP errors over time from wireshark
    st.subheader("TCP errors over time")
    st.write("This graph visualizes the frequency of TCP errors over time, based on the latest PCAP analysis.")

    time_seconds = list(range(0, 350))
    tcp_errors = [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 2, 0, 0, 1,
        0, 0, 0, 0, 0, 2, 0, 0, 0, 0,
        1, 0, 2, 3, 0, 2, 4, 2, 3, 0,
        4, 2, 2, 2, 4, 2, 2, 2, 2, 4,
        4, 2, 4, 3, 3, 4, 3, 2, 4, 3,
        4, 4, 4, 4, 4, 3, 2, 3, 3, 2,
        4, 4, 3, 3, 2, 2, 1, 2, 2, 3,
        4, 2, 1, 4, 3, 3, 2, 1, 3, 4,
        2, 3, 2, 1, 3, 4, 2, 3, 3, 4,
        2, 1, 4, 3, 2, 3, 2, 3, 3, 4,
        3, 4, 2, 3, 2, 3, 3, 2, 4, 2,
        2, 3, 1, 2, 3, 3, 3, 2, 2, 3,
        1, 2, 2, 3, 2, 2, 3, 1, 2, 2,
        1, 2, 3, 2, 2, 3, 3, 1, 1, 3,
        2, 3, 2, 1, 2, 2, 2, 2, 3, 1,
        2, 2, 2, 1, 2, 3, 2, 2, 3, 1,
        1, 1, 2, 3, 2, 1, 1, 2, 2, 2,
        2, 1, 1, 1, 1, 1, 1, 2, 1, 2,
        2, 2, 2, 2, 1, 2, 2, 1, 1, 2,
        2, 2, 1, 1, 2, 1, 2, 2, 1, 2
    ]

    fig, ax = plt.subplots(figsize=(14, 6))
    ax.bar(time_seconds[:len(tcp_errors)], tcp_errors, color='darkred', label='TCP Errors')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Packets/s')
    ax.set_title('TCP Errors Over Time')
    ax.legend()
    st.pyplot(fig)

    st.success("All graphs loaded successfully!")
