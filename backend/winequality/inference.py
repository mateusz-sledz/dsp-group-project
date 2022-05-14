import pandas as pd
import joblib


def make_predictions(data: pd.DataFrame) -> dict[str, str]:
    df_copy = data.copy()
    model = joblib.load('models/RANDOM_FOREST_MODEL')

    return model.predict(df_copy)
