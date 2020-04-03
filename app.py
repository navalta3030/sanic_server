import os

from sanic import Sanic
from sanic import response
from utils import utils, logging

logger = logging.__logger__()

# Set logger to override default basicConfig
sanic = Sanic()

@sanic.route("/")
def test(request):
    logger.info("recedasda'hey'")
    text = "asdasd"
    return response.text(text)

if utils.isDevelopment():
  logger.info("Starting localhost development")
  sanic.run(host="localhost", port=8000, debug=True, auto_reload=True)
else:
  logger.info("Starting production server")
  sanic.run(host="0.0.0.0", port=os.getenv("SANIC_XRAY_PORT"))