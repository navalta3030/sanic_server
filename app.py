import os

from sanic import Sanic
from sanic import response
from utils import utils, logging
from sanic_cors import CORS

logger = logging.__logger__()

# Set logger to override default basicConfig
sanic = Sanic()
CORS(sanic)


@sanic.route("/")
def test(request):
    return response.json({'message': 'Hello world!'})


if utils.isDevelopment():
    logger.info("Starting localhost development")

    sanic.run(host="0.0.0.0", port=8000, debug=True)
else:
    logger.info("Starting production server")
    sanic.run(host="0.0.0.0", port=os.getenv("SANIC_XRAY_PORT"))
