from fastapi import APIRouter
from .endpoints import price
from core import config 

api_prefix = config.API_V1_STR

api_router = APIRouter()
api_router.include_router(price.router, prefix=api_prefix, tags=[api_prefix, 'price'])