from fastapi import (APIRouter, status)

router = APIRouter()

@router.post('/price/inference')
def price_inference():
    return {'message': 'done'}