import sys
sys.path.append("..")
sys.path.append(".")
import pandas as pd
import joblib


def load_pipeline_data() -> pd.DataFrame:
    data = pd.read_csv('backend/data/winequality-red.csv')
    return data


def run_model_background(data: pd.DataFrame) -> dict[str, str]:
    df_copy = data.copy()
    model = joblib.load('backend/models/RANDOM_FOREST_MODEL')
    return model.predict(df_copy)
