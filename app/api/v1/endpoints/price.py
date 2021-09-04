import joblib
import numpy as np
from core import config
# from sklearn.linear_model import LinearRegression
from fastapi import (APIRouter, status)
from pydantic import BaseModel

LM_PATH = config.MODEL_PATH

router = APIRouter()

lm = joblib.load(LM_PATH)


class Item(BaseModel):
    num_rooms: int 
    pupil_teacher_ratio: float 
    l_stat: float 



@router.post('/price/model/inference')
def price_inference(item: Item):
    # Process input request
    data = list(item.dict().values())
    data_array = np.array(data)
    n_features = len(data)
    data_array = data_array.reshape(-1, n_features)

    # Make price prediction
    price_prediction = lm.predict(data_array)
    return {'price': price_prediction[0]}


@router.get('/price/model/info')
def model_info():
    return {'message': 'done'}