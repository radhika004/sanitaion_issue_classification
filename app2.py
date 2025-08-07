

import streamlit as st
import numpy as np
import cv2
import requests
import geocoder
from PIL import Image
from ultralytics import YOLO
import pandas as pd


GOOGLE_API_KEY = "AIzaSyCCneCUHI7BziX3Srwzwtd_1iOqufKglVI"  
model = YOLO("runs\\classify\\train18\\weights\\best.pt")

st.title("Sanitation issue classification")

image_file = st.camera_input("Post issue image")

if image_file:
    image = Image.open(image_file)
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    temp_image_path = "temp_image.jpg"
    cv2.imwrite(temp_image_path, image)
    g = geocoder.ip('me')  
    if g.latlng:
        latitude, longitude = g.latlng

        geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={GOOGLE_API_KEY}"
        response = requests.get(geocode_url).json()

        if response["status"] == "OK":
            address = response["results"][0]["formatted_address"]
        else:
            address = "Address not found"
    else:
        latitude, longitude, address = "Unknown", "Unknown", "Location not available"

    # Run Yolo
    results = model(temp_image_path)
    names_dict = results[0].names
    probs = results[0].probs.tolist()

    predicted_class = names_dict[np.argmax(probs)]
    confidence = max(probs)

    # Display the results
    st.image(image_file, caption="Captured Image", use_column_width=True)
    st.write(f"### Prediction: {predicted_class}")
    st.write(f"### Confidence: {confidence:.2f}")
    
    # Handle address not found
    if address == "Address not found":
        st.write(f"### Address: Unable to retrieve address (Latitude: {latitude}, Longitude: {longitude})")
    else:
        st.write(f"### Address: {address}")

    # Display the map if location is available
    if latitude != "Unknown" and longitude != "Unknown":
        location_data = pd.DataFrame({
            'latitude': [latitude],
            'longitude': [longitude]
        })

        #  map
        st.map(location_data)

        # Provide a link to view location on Google Maps
        st.markdown(f"[📍 View on Google Maps](https://www.google.com/maps/search/?api=1&query={latitude},{longitude})")
