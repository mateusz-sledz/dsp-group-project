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


# class Config:
# 	arbitrary_types_allowed = True


@app.post("/predict", response_model=Response)
async def predict(file: UploadFile = File(...)):
    data = pd.read_csv(StringIO(str(file.file.read(), 'utf-8')), header=None, encoding='utf-8')
    # data = np.array(data)
    return Response(make_predictions(data))
