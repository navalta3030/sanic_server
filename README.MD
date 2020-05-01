# Getting started ![Production](https://github.com/navalta3030/sanic_server/workflows/Production/badge.svg) ![Staging](https://github.com/navalta3030/sanic_server/workflows/Staging/badge.svg)

- Creating virtual environment and activate
```
python3 -m venv .env
source .env/Scripts/activate
```

- Installing dependencies
```
pip install requirements.txt
```

- Starting the application
```
python app.py
```

# Available Routes

| Route         | Description                                 | Method  |
| ------------- |:-------------------------------------------:| -----:  |
| /test         | Health check                                |  GET    |
| /predictImage | Predicting image sent                       |  POST   |

# Prediction Overview
- Pneumonia --> 92% accuracy
  - trained on 6000 datasets, 50% pneumonia and 50% normal.


