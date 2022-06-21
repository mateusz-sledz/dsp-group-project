import random
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
from backend.winequality.train import build_model
from backend.winequality.inference import make_predictions


def load_pipeline_data():
    if os.getenv('ROOT') is None:
        load_dotenv()

    data = pd.read_csv(os.getenv('ROOT') + '/backend/data/winequality-red.csv')
    data.drop(columns=['quality'], inplace=True)

    row = np.array(data.loc[random.randint(0, len(data) - 1)]).reshape(1, -1)
    return row


def run_model_background(data) -> dict[str, str]:
    return make_predictions(data)


def get_data_for_retraining():
    if os.getenv('ROOT') is None:
        load_dotenv()
    return pd.read_csv(os.getenv('ROOT') + '/backend/data/winequality-red.csv')


def retrain_model(data):
    return build_model(data)
