# SwarNeTT

SwarNeTT is an innovative communication library that leverages Wi-Fi Direct technology to establish secure, decentralized networks among nearby devices. It is designed to function without internet connectivity, making it ideal for disaster management and large-scale communication systems.

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Performance Evaluation](#performance-evaluation)
- [Competitive Analysis](#competitive-analysis)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)

## Overview

SwarNeTT was presented during the Research Festival and Principal’s Research Awards hosted at the University of the West Indies, St. Augustine, on November 22nd and 23rd, 2023. Developed by Dr. Wayne Goodridge and Lead Programmer Kwasi Edwards, SwarNeTT is designed to facilitate communication in areas where internet access is unavailable or unreliable.

The system utilizes Wi-Fi Protected Setup (WPS) and Wi-Fi Protected Access (WPA) protocols to ensure secure communication. SwarNeTT supports inter-group communication and is adaptable to geographically widespread networks.

## Key Features

- **Wide-Area Coverage**: SwarNeTT can transmit messages across large geographic areas, ensuring urban and rural locations receive crucial updates.
- **Combating Fake News**: Incorporates systems to detect and filter fake news, ensuring accurate information during emergencies.
- **Future-Proof Communication**: Can eventually integrate with the internet as infrastructure improves.
- **Seamless Connectivity**: The network can automatically connect nearby devices, ensuring consistent communication even with some devices out of range.
- **Topic-Based Alerts**: Receive targeted messages based on specific disaster-related topics like hurricanes, earthquakes, and flooding.

## Performance Evaluation

SwarNeTT has been rigorously tested under realistic conditions to evaluate its reliability as a disaster communication network.

Scenarios include:

- **Idle state**
- **Moderate load**
- **Heavy network traffic**

These tests were conducted across various geographic locations to observe stability, latency, and overall network performance in the absence of traditional infrastructure.

## Competitive Analysis

In addition to technical testing, SwarNeTT was compared against existing communication tools to assess its place in the market. Metrics such as message delivery success rate, transmission delays, and connection robustness were benchmarked, providing valuable insights into SwarNeTT’s unique strengths and areas for growth in the emergency communication space.

## Installation

To get started with SwarNeTT, clone this repository and install the necessary dependencies.

1. Clone the repository:
   ```bash
   git clone https://github.com/SYNergyOrganization/SYNergy-Code-for-Final-Year-Project

## Usage

Running the Application
You can start the SwarNeTT application using Streamlit for the frontend visualization and analysis:
    ```bash
    cd SYNergy-Code-for-Final-Year-Project/streamlit_app
    streamlit run app.py

## File Structure

streamlit_app/
├── data/
│   ├── packetsTransmissionFinalResults.csv
│   ├── packetsTransmittedInitialResults.csv
│   ├── tcpErrorFinalResults.csv
│   └── tcpErrorInitialResults.csv
│
├── pages/
│   ├── competitors.py
│   ├── finalresults.py
│   ├── home.py
│   └── initialresults.py
│
├── app.py
├── .gitignore
├── README.md
├── requirements.txt
└── venv/  (virtual environment)