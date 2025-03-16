import logging

# Configuration du logger
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s",
                    encoding="utf-8")


def log_info(message):
    logging.info(message)


def log_error(message):
    logging.error(message)
