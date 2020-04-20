FROM  tensorflow/tensorflow:latest-py3

COPY requirements.txt /requirements.txt
RUN python3 -m pip install -r requirements.txt && mkdir /app


COPY . /app

# RUN Testing
WORKDIR /app
RUN python3 __test__/test_ml.py

ENTRYPOINT ["python3", "app.py"]
