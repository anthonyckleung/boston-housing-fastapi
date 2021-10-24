FROM continuumio/miniconda3:4.10.3

RUN mkdir -p /mlflow/mlruns

WORKDIR /mlflow

# ENV LC_ALL=C.UTF-8
# ENV LANG=C.UTF-8

# RUN echo "export LC_ALL=$LC_ALL" >> /etc/profile.d/locale.sh
# RUN echo "export LANG=$LANG" >> /etc/profile.d/locale.sh
# ENV GUNICORN_CMD_ARGS="--timeout 500"

RUN apt-get update && apt-get install -y \
    build-essential \
    # python3-dev \
    # libpq-dev
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
# RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt
# RUN pip install -U pip && \
#     # pip install --ignore-installed google-cloud-storage && \
#     # pip install boto3 psycopg2 mlflow==1.9.1 && \
#     # pip install gunicorn==19.9.0
#     pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

# COPY ./start.sh ./start.sh
# RUN chmod +x ./start.sh

COPY ./scripts/start_mlflow_server.sh ./start_mlflow_server.sh
RUN chmod +x ./start_mlflow_server.sh

# EXPOSE 80
# EXPOSE 5000

# CMD ["./start_mlflow_ui.sh"]