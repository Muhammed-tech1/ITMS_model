import streamlit as st
import pandas as pd
import joblib
#import os
import datetime

# Load model
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#model = joblib.load(os.path.join(BASE_DIR, "traffic_model.pkl"))

model = joblib.load("traffic_model.pkl")

st.set_page_config(page_title="Intelligent Traffic Management System", layout="wide")

st.title("🚦 Intelligent Traffic Management System")
st.markdown("### Real-Time Traffic Prediction & Monitoring Dashboard")

st.sidebar.header("Input Traffic Parameters")

# Sidebar inputs
car = st.sidebar.number_input("Car Count", min_value=0, value=50)
bike = st.sidebar.number_input("Bike Count", min_value=0, value=20)
bus = st.sidebar.number_input("Bus Count", min_value=0, value=10)
truck = st.sidebar.number_input("Truck Count", min_value=0, value=5)

total = car + bike + bus + truck

date = st.sidebar.date_input("Date", datetime.date.today())
time = st.sidebar.time_input("Time", datetime.datetime.now().time())

dt = datetime.datetime.combine(date, time)

# Feature extraction
year = dt.year
month = dt.month
day = dt.day
hour = dt.hour
dayofweek = dt.weekday()

X_input = pd.DataFrame([[car, bike, bus, truck, total,
                          year, month, day, hour, dayofweek]],
                        columns=['CarCount','BikeCount','BusCount','TruckCount',
                                 'Total','year','month','day','hour','dayofweek'])

# Prediction
if st.sidebar.button("Predict Traffic"):
    prediction = model.predict(X_input)[0]

    st.subheader("Prediction Result")

    if prediction == "Heavy":
        st.error("🚨 Heavy Traffic Detected")
    elif prediction == "Normal":
        st.warning("⚠ Normal Traffic")
    else:
       st.success("✅ Low Traffic")

    st.write("### Prediction:", prediction)

st.markdown("---")

# Dashboard preview
st.subheader("📊 Traffic Analytics Dashboard")
df = pd.read_csv("Traffic.csv")

st.line_chart(df[['CarCount','BikeCount','BusCount','TruckCount']].head(100))

st.bar_chart(df['Traffic Situation'].value_counts())

st.success("System Running Successfully 🚀")