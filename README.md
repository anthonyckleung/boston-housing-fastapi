# Boston Housing Price Model - FastAPI Demo

Expose a trained and saved [linear regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) model with FastAPI.


The Boston house-prices dataset was used to train the model. From EDA only 3 features are selected for modeling, namely: `RM`, `PTRATIO`, and `LSTAT`. Refer to notebook found in `notebooks/boston-housing.ipynb`.



## Install Requirements

```
pip install -r requirements.txt
```

## Run the Server:

```
cd app
uvicorn main:app --reload
```

Then go to http://localhost:8000/api/v1/docs

![](imgs/fastapi_docs.png)