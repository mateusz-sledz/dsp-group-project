import requests
import streamlit as st
import pandas as pd
import numpy as np
import sys
sys.path.append("..")
from backend.postgres_handler.connector import get_from_db
import streamlit.components.v1 as components
from st_aggrid import AgGrid


FEATURES = ['f_acidity', 'v_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'sulfur_dioxide',
            't_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol']

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

st.title("Wine quality prediction - web app")

file = st.file_uploader("Choose a CSV file with data")

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


with st.form("my_form"):
    st.write("Provide data for prediction")

    values = [0]*len(FEATURES)
    for i, v in enumerate(FEATURES):
        values[i] = st.number_input(v, 0.0, 100.0)

    values_list = [values]
    submitted = st.form_submit_button("Submit")

    if submitted:
        to_send = []

        for instance in values_list:
            to_send.append(dict(zip(FEATURES, instance)))

        response = requests.post("http://127.0.0.1:8000/predict", json=to_send)

        if response.status_code != 200:
            st.error("Wrong data provided")
        else:
            predictions = response.json().get("predictions")
            st.caption('Predictions')
            st.text(predictions[0])


def show_pred():
    data_pred = get_from_db()
    df = pd.DataFrame(data_pred, columns =['fixed_acidity',
                                    'volatile_acidity',
                                    'citric_acid',
                                    'residual_sugar',
                                    'chlorides',
                                    'free_sulfur_dioxide',
                                    'total_sulfur_dioxide',
                                    'density',
                                    'pH',
                                    'sulphates',
                                    'alcohol',
                                    'quality'
                                    ])
    AgGrid(df)

st.title("Past Predictions")

button_flag = 'button_flag'
reload = False
if button_flag not in st.session_state:
    st.session_state[button_flag] = False

if st.session_state[button_flag]:
    myBtn = st.button('Reload')
    st.session_state[button_flag] = True
    show_pred()
else:
    myBtn = st.button('Show')
    st.session_state[button_flag] = True
    
