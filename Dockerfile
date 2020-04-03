FROM python:3.7-slim-stretch
RUN apt-get update && apt-get -y install gcc

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT ["python", "/app/app.py"]