
import pandas as pd
import joblib


def load_pipeline_data() -> pd.DataFrame:
    data = pd.read_csv('../backend/data/injection_data1.csv')
    return data


def run_model_background(data: pd.DataFrame) -> dict[str, str]:
    df_copy = data.copy()
    model = joblib.load('../backend/models/RANDOM_FOREST_MODEL')
    return model.predict(df_copy)
