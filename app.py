import os

from sanic import Sanic
from sanic import response
from utils import utils
from sanic.log import logger
from sanic_cors import CORS
from ml_modules.tensorflow_img import TensorflowImg

import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# Set logger to override default basicConfig
sanic = Sanic()
# CORS(sanic)

TF = TensorflowImg()


@sanic.route("/test")
def test(request):
    return response.json({'message': 'Hello world!'})


@sanic.route("/predictImage", methods=['POST'])
def predict(request):
    file = request.files['file']
    prediction = TF.predict(file[0])

    return response.json({'answer': prediction})


if utils.isDevelopment():
    logger.info("Starting localhost development")

    sanic.run(host="0.0.0.0", port=8000, debug=True, access_log=True)

else:
    logger.info("Starting production server")
    sanic.run(host="0.0.0.0", port=os.getenv(
        "SANIC_XRAY_PORT"), access_log=True)
