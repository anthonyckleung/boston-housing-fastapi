import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.datasets import load_boston
from urllib.parse import urlparse


# Seed everything
np.random.seed(45)

# Load Dataset
boston = load_boston()
# Initializing the dataframe
data = pd.DataFrame(boston.data)
data.columns = boston.feature_names

#Adding target variable to dataframe
data['PRICE'] = boston.target


def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


def train():
    # Spliting target variable and independent variables
    X = data.drop(['PRICE'], axis = 1)
    y = data['PRICE']

    X = X[['RM', 'PTRATIO', 'LSTAT']]

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 42)

    with mlflow.start_run():
        # Create a Linear regressor
        lm = LinearRegression()

        # Train the model using the training sets 
        lm.fit(X_train, y_train)
        y_pred = lm.predict(X_test)

        (rmse, mae, r2) = eval_metrics(y_test, y_pred)

        print("  RMSE: %s" % rmse)
        print("  MAE: %s" % mae)
        print("  R2: %s" % r2)

        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)
        mlflow.log_metric("mae", mae)

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # Model registry does not work with file store
        if tracking_url_type_store != "file":

            # Register the model
            # There are other ways to use the Model Registry, which depends on the use case,
            # please refer to the doc for more information:
            # https://mlflow.org/docs/latest/model-registry.html#api-workflow
            mlflow.sklearn.log_model(lm, "model", registered_model_name="LR_Boston_House_Model")
        else:
            mlflow.sklearn.log_model(lm, "model")




if __name__=="__main__":
    train()
