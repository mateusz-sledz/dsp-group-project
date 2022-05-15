import requests
import streamlit as st
import json
import pandas as pd

FEATURES = ['f_acidity', 'v_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'sulfur_dioxide',
            't_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol']
# import features from backend

STYLES = {
    "candy": "candy",
    "composition 6": "composition_vii",
    "feathers": "feathers",
    "la_muse": "la_muse",
    "mosaic": "mosaic",
    "starry night": "starry_night",
    "the scream": "the_scream",
    "the wave": "the_wave",
    "udnie": "udnie",
}

st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.title("ML web app")

# displays a file uploader widget
file = st.file_uploader("Choose a CSV file with data")

# displays a button
if st.button("Predict"):
    if file is not None:
        
        try:
            data = pd.read_csv(file, header=None)
        except:
            print("sth went wrong", data)

        values_list = data.values.tolist()
        to_send = []

        for instance in values_list:
            to_send.append(dict(zip(FEATURES, instance)))

        response = requests.post("http://127.0.0.1:8000/predict", json=to_send)

        if response.status_code != 200:
            st.error("Wrong data provided")
        else:
            predictions = response.json().get("predictions")
            st.text_area(value=predictions, label='Predictions')



