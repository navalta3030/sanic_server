import logging


def __logger__():
    """
    Initialize the logger
    """
    logger = logging.getLogger(__name__)
    logging_format = "[%(asctime)s] - %(levelname)s "
    logging_format += "%(module)s::%(funcName)s():l%(lineno)d: "
    logging_format += "%(message)s"

    logging.basicConfig(
        filename="logs.log",
        format=logging_format,
        level=logging.DEBUG
    )

    return logger
