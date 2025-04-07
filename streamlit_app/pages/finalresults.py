import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


def finalresults_page():
    st.markdown("<h1 style='font-size: 50px; color:#FF5733;'>Final Results</h1>", unsafe_allow_html=True)
    st.write("""
        These are the final results of the SwarNeTT system after further testing with high-traffic and multiple user scenarios.
    """)

    # Users connected and disconnected pie chart
    st.subheader("Users Connected and Disconnected")
    st.write("This pie chart shows the number of users successfully connected and disconnected on Wi-Fi Direct.")
    
    labels = ['Connected', 'Disconnected']
    sizes = [4, 4]
    colors = ['#66b3ff', '#ff6666']
    explode = (0.1, 0)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    ax.axis('equal')
    st.pyplot(fig)

    st.write("""
        The application successfully connected 8 users on Wi-Fi Direct but disconnected them due to network conditions. 
        4 users were later reconnected, although they experienced delays in receiving messages.
    """)

    # Distance coverage
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

    st.write("Addition of users did not impact the Final distance results.")

    # *Wi-Fi Direct & System Performance Analysis*
    st.subheader("Wi-Fi Direct & System Performance Analysis")
    st.write("This section visualizes packet transmission, TCP errors, packet loss, throughput from PCAPdroid and analyzed by WireShark. Energy Used was determined using Android Studio.")

    # Packet Transmission Graph
    packetsTransmittedFinalResults_df = pd.read_csv('data\packetsTransmissionFinalResults.csv')

    time_span = packetsTransmittedFinalResults_df['Interval start']
    packets_per_second = packetsTransmittedFinalResults_df['All Packets']

    st.subheader("Packet Transmission Over Time")
    fig, ax = plt.subplots()
    ax.plot(time_span, packets_per_second, marker='o', linestyle='-', color='b', label='Packets per Second')
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Packets per Second')
    ax.set_title('Wi-Fi Direct Packet Transmission')
    ax.legend()
    ax.grid()
    ax.set_xticks(time_span[::25])  # spread out every 5th label
    plt.xticks(rotation=45)        # rotate for readability
    ax.set_xlim(min(time_span), max(time_span))
    st.pyplot(fig)

    # TCP Errors Graph
    tcpErrorFinalResults_df = pd.read_csv('data/tcpErrorFinalResults.csv')

    time_span = tcpErrorFinalResults_df['Interval start']
    tcp_errors = tcpErrorFinalResults_df['TCP Errors']

    st.subheader("TCP Errors Over Time")
    st.write("This graph visualizes the frequency of TCP errors over time, based on the latest PCAP analysis.")
    fig, ax = plt.subplots()
    ax.bar(time_span, tcp_errors, color='r', label='TCP Errors')
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Number of TCP Errors')
    ax.set_title('Wi-Fi Direct TCP Errors')
    ax.legend()
    ax.set_xticks(time_span[::25])  # show every 5th label to spread out x-axis
    plt.xticks(rotation=45)
    ax.set_xlim(min(time_span), max(time_span))
    st.pyplot(fig)


    # Throughput over time
    st.subheader("Throughput Over Time")

    throughput = [
        6333, 8620, 4518, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 80, 0, 0, 80,
        400, 0, 200, 0, 0, 0, 100, 100, 0, 0,
        0, 0, 0, 0, 0, 200, 0, 0, 0, 0,
        0, 0, 400, 0, 200, 0, 0, 0, 200, 0,
        0, 200, 0, 0, 0, 400, 100, 300, 0, 0,
        0, 500, 100, 200, 400, 0, 200, 200, 0, 0,
        400, 0, 100, 100, 200, 400, 0, 200, 0, 200,
        0, 200, 0, 200, 0, 0, 200, 0, 0, 600,
        0, 400, 0, 400, 0, 400, 200, 0, 0, 200,
        0, 0, 0, 0, 600, 200, 400, 100, 100, 0,
        200, 0, 0, 0, 400, 400, 200, 200, 300, 0,
        700, 400, 200, 500, 300, 200, 200, 0, 200, 500,
        100, 0, 0, 0, 400, 0, 0, 0, 200, 600,
        0, 200, 0, 0, 0, 500, 100, 0, 0, 0,
        600, 0, 200, 200, 400, 0, 200, 200, 0, 0,
        0, 0, 0, 0, 600, 0, 200, 200, 0, 0,
        200, 200, 0, 0, 0, 0, 0, 200, 0, 200,
        400, 0, 0, 0, 200, 0, 0, 0, 200, 400,
        0, 200, 0, 0, 0, 200, 200, 0, 0, 0,
        0, 200, 400, 100, 300, 0, 0, 0, 200, 0,
        0, 0, 200, 0, 400, 0, 400, 0, 0, 0,
        400, 0, 0, 0, 0, 0, 0, 0, 0, 400,
        0, 0, 200, 0, 0, 0, 0, 0, 0, 400,
        0, 200, 0, 0, 0, 200, 200, 0, 0, 0,
        0, 0, 0, 200, 200, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 400, 0, 400, 0, 0, 0,
        300, 100, 0, 0, 0, 0, 0, 0, 200, 200,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 400,
        0, 200, 0, 0, 0, 400, 0, 0, 0, 0,
        0, 0, 200, 0, 200, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        200, 0, 0, 0, 0, 0, 0, 100, 0, 100,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 200
    ]


    df = pd.DataFrame({
        "Interval": range(len(throughput)),
        "Throughput": throughput
    })

    fig, ax = plt.subplots(figsize=(14, 5))
    ax.plot(df["Interval"], df["Throughput"], color="mediumblue", linewidth=1.5)
    ax.set_title("Network Throughput Over Time", fontsize=16)
    ax.set_xlabel("Time Interval (s)")
    ax.set_ylabel("Throughput (Bytes/sec)")
    ax.grid(True, linestyle="--", alpha=0.5)
    st.pyplot(fig)

    # Battery usage at idle
    st.subheader("Battery Consumption while app is idling")
    st.write("This bar chart shows the average power usage (in mW) by each system component while SwarNeTT is idle for approximately 5 minutes.")

    labels_idle = ["CPU Big", "Display", "WLAN", "CPU Little", "Memory", "Sensor Core", "UFS (Disk)", "Cellular", "CPU Mid", "GPU", "Camera", "GPS"]
    power_idle = [1218.32, 452.24, 236.89, 178.06, 44.42, 27.28, 26.69, 19.09, 20.51, 4.03, 0.64, 0]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(labels_idle, power_idle, color='skyblue')
    ax.set_xlabel('Power Consumption (mW)')
    ax.set_title('Idle: Average Power Consumption by Component')
    st.pyplot(fig)

    # Battery usage under load
    st.subheader("Battery Consumption while app is under load")
    st.write("This bar chart shows the average power usage (in mW) by each system component while SwarNeTT is actively being used for approximately 5 minutes.")

    power_load = [1202.04, 455.05, 231.36, 200.22, 58.7, 28.19, 26.25, 18.19, 11.1, 7.15, 0.95, 0]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(labels_idle, power_load, color='salmon')  
    ax.set_xlabel('Power Consumption (mW)')
    ax.set_title('Under Load: Average Power Consumption by Component')
    st.pyplot(fig)

    st.success("Final Results Complete")






