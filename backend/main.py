from fastapi import FastAPI
import pandas as pd
import numpy as np
from fastapi import File
from fastapi import UploadFile
from io import StringIO
from pydantic import BaseModel
from winequality.inference import make_predictions


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

    pred = list(make_predictions(np.array(features)))

    return Response(predictions=pred)



