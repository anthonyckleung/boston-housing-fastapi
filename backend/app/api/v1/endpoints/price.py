import joblib
import numpy as np
from core import config
from fastapi import (APIRouter, status)
from models.schema import Item 

LM_PATH = config.MODEL_PATH

router = APIRouter()

lm = joblib.load(LM_PATH)
feature_list = ['RM', 'PTRATIO', 'LSTAT']


@router.post('/price/model/inference')
def price_inference(item: Item):
    # Process input request
    data = list(item.dict().values())
    data_array = np.array(data)
    n_features = len(data)
    data_array = data_array.reshape(-1, n_features)

    # Make price prediction
    price_prediction = lm.predict(data_array)
    payload = dict(
        query = item.dict(),
        price = round(price_prediction[0], 2) * 1000  # N.b. Value was in 1000s
    )
    return payload


@router.get('/price/model/info')
async def model_info():
    estimator_type = lm._estimator_type
    coefficients = dict(zip(feature_list,lm.coef_))

    payload = dict(
        estimator = estimator_type,
        coefficients = coefficients
    )
    return payload
