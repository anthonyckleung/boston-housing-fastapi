import uvicorn
from fastapi import FastAPI
from core import config

# from api.api_v1.api import api_router

app = FastAPI(title=config.PROJECT_NAME, 
            openapi_url="/api/v1/openapi.json",
            docs_url="/api/v1/docs",
            redoc_url="/api/v1/redoc"
            )

# CORS
origins = []

@app.get("/")
async def root():
    return {"message": "Hello Boston"}

if __name__== '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')
