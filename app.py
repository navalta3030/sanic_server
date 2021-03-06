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
    """
    Responsible for the prediction of the image

    @return - [<filename>, <prediction_label>, <prediction_accuracy>]
    """
    file = request.files['file']
    retVal = TF.predict(file)
    return response.json({'data': retVal})


if utils.isDevelopment():
    logger.info("Starting localhost development")

    sanic.run(host="0.0.0.0", port=8000, debug=True, access_log=True)

else:
    logger.info("Starting production server")
    sanic.run(host="0.0.0.0", port=os.getenv(
        "SANIC_XRAY_PORT"), access_log=True)
