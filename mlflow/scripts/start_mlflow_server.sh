#!/bin/bash

mlflow server \
    --backend-store-uri $DB_URI \
    --host 0.0.0.0 \
    --port 5000 \
    --default-artifact-root $MLFLOW_ARTIFACT_ROOT