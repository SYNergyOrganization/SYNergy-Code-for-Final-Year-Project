import streamlit as st

def homepage():
    st.markdown("<h1 style='font-size: 50px; color:#FF5733;'>SwarNeTT</h1>", unsafe_allow_html=True)
    st.write("""
        On November 22nd and 23rd, 2023, during the Research Festival and Principal’s Research Awards hosted at the University of the West Indies, St. Augustine, 
        Dr. Wayne Goodridge, Head of the Department of Computing and Information Technology, and Lead Programmer Kwasi Edwards revealed SwarNeTT, an innovative communication library.
    """)
    st.write("""
        SwarNeTT leverages Wi-Fi Direct technology to form a secure, decentralized network among nearby devices, without using internet connectivity. Wi-Fi Direct systems utilize 
        Wi-Fi Protected Setup (WPS) and Wi-Fi Protected Access (WPA) protocols to ensure robust security. 
        It also utilizes a publish-subscribe protocol, a decoupled messaging architecture that allows publishers to send messages based on predefined topics without needing a direct 
        connection to subscribers.
    """)
    st.write("""
        SwarNeTT is not only innovative in its use of Wi-Fi Direct but also incorporates inter-group communication and supports large-scale, geographically widespread networks.
    """)

    st.markdown("<h2 style='font-size: 40px; color:#FF5733;'>Key Features of SwarNeTT</h2>", unsafe_allow_html=True)
    st.write("""
        Some advanced features of SwarNeTT tailored for Natural Disaster Management include:
    """)

    features = [
        ("Wide-Area Coverage", "Messages can be transmitted across large geographic regions, ensuring that both urban and rural areas receive crucial updates and alerts."),
        ("Combating Fake News", "The system incorporates mechanisms to detect and filter fake news, ensuring only accurate information is available, thereby reducing panic and misinformation."),
        ("Future-Proof Communication", "SwarNeTT can eventually connect to the Internet when it becomes available, ensuring continuous and reliable communication as infrastructure is restored."),
        ("Seamless Connectivity", "The system can automatically connect to other devices nearby, allowing the network to function and relay messages even if some devices are out of range."),
        ("Topic-Based Alerts", "Users receive messages categorized by specific disaster-related topics, such as flooding, earthquakes, or hurricanes, ensuring useful and timely updates."),
    ]

    for feature, description in features:
        st.write(f"**{feature}:** {description}")