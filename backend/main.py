from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel
from winequality.inference import make_predictions
from postgres_handler.connector import save_to_db


app = FastAPI()


class Response(BaseModel):
    predictions: list[int]


class Request(BaseModel):
    f_acidity: float
    v_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    sulfur_dioxide: float
    t_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float
    
    class Config:
        orm_mode = True


@app.post("/predict", response_model=Response)
async def predict(data: list[Request]):
    features = []

    for row in data:
        features.append([x[1] for x in list(row)])

    pred = (make_predictions(np.array(features))).tolist()

    for f, p in zip(features, pred):
        f.append(p)

    save_to_db(features)

    return Response(predictions=pred)



