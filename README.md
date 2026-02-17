#🚦 Intelligent Traffic Management System Using Real-Time Data Analytics
Final Year Project — Computer Science

Author: Muhammed Abdullahi

📌 Project Overview

This project presents the design and implementation of an Intelligent Traffic Management System (ITMS) that leverages machine learning, real-time data analytics, and interactive visualization to predict traffic conditions and support efficient traffic control decisions.

The system analyzes traffic data collected from sensors and monitoring systems to classify traffic situations as Low, Normal, or Heavy, providing actionable insights for traffic authorities.

A web-based dashboard built using Streamlit enables real-time prediction, monitoring, and visualization.

🎯 Objectives

Develop a predictive traffic management system using machine learning.

Analyze traffic flow patterns using real-world datasets.

Design a real-time web-based dashboard for traffic monitoring.

Improve traffic control efficiency and congestion management.

📊 Dataset Description

Source: Kaggle – Traffic Flow Dataset

Dataset Size: ~3,000 records

Nature: Real-world traffic flow data

Data Type: Tabular time-series traffic counts

Key Features Used
Feature	Description
CarCount	Number of cars detected
BikeCount	Number of bikes detected
BusCount	Number of buses detected
TruckCount	Number of trucks detected
Total	Total number of vehicles
Year	Extracted from datetime
Month	Extracted from datetime
Day	Extracted from datetime
Hour	Extracted from datetime
DayOfWeek	Extracted from datetime
Target Variable

Traffic Situation → Low, Normal, Heavy

🧠 Machine Learning Model

Algorithm Used: Random Forest Classifier

Model Accuracy: 98%

Why Random Forest?

High performance on structured tabular data

Handles nonlinear relationships efficiently

Provides excellent accuracy and robustness

⚙️ System Architecture
Traffic Dataset → Data Preprocessing → Feature Engineering → ML Model → 
Streamlit Web Dashboard → Real-Time Prediction & Visualization

🖥️ System Features

Real-time traffic condition prediction

Interactive web dashboard

Live input parameter control

Data visualization charts

Smart congestion level classification

🚀 Deployment

The system is deployed locally using Streamlit, enabling:

Interactive predictions

Traffic analytics visualization

Real-time simulation of traffic scenarios

Run the application:

streamlit run app.py

🏫 Academic Context

This project was developed as a Final Year Project (FYP) in partial fulfillment of the requirements for the award of Bachelor of Science (B.Sc.) in Computer Science.

Institution: Lagos State University (LASU)

🛠 Technologies Used

Python

Pandas

NumPy

Scikit-learn

Streamlit

Matplotlib

Machine Learning

📌 Author

Muhammed Abdullahi
Final Year Computer Science Student
Aspiring Data Scientist & Machine Learning Engineer

⭐ Acknowledgment

Special thanks to my project supervisor (DR.ADENOWO) and lecturers for their guidance and academic support throughout the development of this system.
