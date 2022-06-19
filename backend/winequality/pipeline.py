import random
import pandas as pd
import numpy as np
from backend.winequality.train import build_model
from backend.winequality.inference import make_predictions



def load_pipeline_data() -> pd.DataFrame:
    data = pd.read_csv('backend/data/winequality-red.csv')
    data.drop(columns=['quality'], inplace=True)

    row = np.array(data.loc[ random.randint(0, len(data) - 1) ]).reshape(1, -1)
    return row


def run_model_background(data) -> dict[str, str]:
    # df_copy = data.copy()
    # model = joblib.load('backend/models/RANDOM_FOREST_MODEL')
    return make_predictions(data)


def get_data_for_retraining():
    return pd.read_csv('backend/data/winequality-red.csv')


def retrain_model(data):
    return build_model(data)
