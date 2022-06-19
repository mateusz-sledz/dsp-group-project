import os
from dotenv import load_dotenv
import pandas as pd
import joblib


def make_predictions(data: pd.DataFrame) -> dict[str, str]:
    if os.getenv('ROOT') is None:
        load_dotenv()

    df_copy = data.copy()
    model = joblib.load(os.getenv('ROOT')+'/backend/models/RANDOM_FOREST_MODEL')

    return model.predict(df_copy)
