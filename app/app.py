import streamlit as st
import pickle
import numpy as np

# Load model
with open('./models/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('./models/columns.pkl', 'rb') as f:
    feature_names = pickle.load(f)

st.title("Food Delivery Time Estimator")

user_input = []

delivery_rating = st.slider("Enter Delivery_person_Ratings", 0.0, 5.0, step=0.1)
user_input.append(delivery_rating)

weather_options = {
    "Sunny": 0,
    "Cloudy": 1,
    "Windy": 2,
    "Fog": 3,
    "Stormy": 4,
    "Sandstorms": 5
}
weather = st.selectbox("Enter Weather_conditions", options=list(weather_options.keys()))
user_input.append(weather_options[weather])

traffic_options = {
    "Low": 0,
    "Medium": 1,
    "High": 2,
    "Jam": 3
}
traffic = st.selectbox("Enter Road_traffic_density", options=list(traffic_options.keys()))
user_input.append(traffic_options[traffic])

vehicle_condition = st.slider("Enter Vehicle_condition", 0, 2)
user_input.append(vehicle_condition)

multiple_deliveries = st.slider("Enter multiple_deliveries", 0, 3)
user_input.append(multiple_deliveries)

festival_options = {"No": 0, "Yes": 1}
festival = st.selectbox("Is there a Festival?", list(festival_options.keys()))
user_input.append(festival_options[festival])

city_options = {
    "Urban": 0,
    "Semi-Urban": 1,
    "Metropolitan": 2
}
city = st.selectbox("Enter City", list(city_options.keys()))
user_input.append(city_options[city])

distance = st.number_input("Enter Distance (km)", min_value=0.0, step=0.1)
user_input.append(distance)

prep_time = st.number_input("Enter prep_time", min_value=0.0, step=0.1)
user_input.append(prep_time)

hour_of_day = st.slider("Enter hour_of_day", 0, 23)
user_input.append(hour_of_day)


if st.button("Predict Delivery Time"):
    prediction = model.predict([user_input])[0]
    st.success(f"Estimated Delivery Time: {round(prediction, 2)} minutes")
