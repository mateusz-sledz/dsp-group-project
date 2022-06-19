import pandas as pd
import joblib
import os


def make_predictions(data: pd.DataFrame) -> dict[str, str]:
    df_copy = data.copy()
    model = joblib.load(os.getenv('ROOT')+'/backend/models/RANDOM_FOREST_MODEL')

    return model.predict(df_copy)
