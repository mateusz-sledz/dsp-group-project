import requests
import streamlit as st

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
data = st.file_uploader("Choose a CSV file with data")


# displays a button
if st.button("Predict"):
    if data is not None:
        file = {"file": data.getvalue()}
        res = requests.post("http://127.0.0.1:8000/predict", files=file)

        predictions = res.json().get("predictions")
        st.text_area(value=predictions, label='Predictions')
