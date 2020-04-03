FROM  python:3.7-slim-buster
RUN apt update

COPY requirements.txt /requirements.txt
RUN python3 -m pip install -r requirements.txt && mkdir /app

COPY . /app
WORKDIR /app

ENTRYPOINT ["python3", "app.py"]