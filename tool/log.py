
from logging import getLogger, Formatter, StreamHandler, INFO, DEBUG
from logging import Logger

def build_logger(module, debug=False):
    # avoid duplication
    Logger.manager.loggerDict.pop(module, None)
    # setUp
    _logger = getLogger(module)
    _logger = _set_handler(_logger, StreamHandler(), debug)
    _logger.setLevel(DEBUG)
    _logger.propagate = False
    return _logger

def _set_handler(logger, handler, debug):
    if debug:
        handler.setLevel(DEBUG)
    else:
        handler.setLevel(INFO)
    handler.setFormatter(
        Formatter(
            '%(asctime)s.%(msecs)-3d %(name)s:%(lineno)s %(funcName)s [%(levelname)s]: %(message)s',
            datefmt='%H:%M:%S',
        ))
    logger.addHandler(handler)
    return logger
