# Boston Housing Price Model - FastAPI Demo

[![CI](https://github.com/anthonyckleung/boston-housing-fastapi/actions/workflows/main.yml/badge.svg)](https://github.com/anthonyckleung/boston-housing-fastapi/actions/workflows/main.yml)

**(2021-10-24)**: Working towards setting up MLFlow as a separate service to model inference. Remains work-in-progress.


Expose a trained and saved [linear regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) model with [FastAPI](https://fastapi.tiangolo.com/).

The Boston house-prices dataset was used to train the model. From EDA only 3 features are selected for modeling, namely: `RM`, `PTRATIO`, and `LSTAT`. Refer to notebook found in `notebooks/boston-housing.ipynb`.


## Build and Run the Stack
```
docker-compose up
```


<!-- ## Alternative: Run with Docker

Build the image:
```
$ docker build -t myimage .
```

Start the Docker container:
```
$ docker run -p 8000:8000 myimage
``` -->

<!-- ![](imgs/fastapi_docs.png) -->
