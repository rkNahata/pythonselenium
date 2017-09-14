import logging
import inspect

def customLoger(logLevel=logging.DEBUG):

    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log", "a")
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m%d%Y %H:%M%S')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
