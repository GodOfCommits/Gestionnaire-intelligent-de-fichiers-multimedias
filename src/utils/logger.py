import logging

# Configuration du logger
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s",
                    encoding="utf-8")


def log_info(message):
    logging.info(message)


def log_error(message):
    logging.error(message)


# Test
log_info("Application démarrée.")
log_error("Erreur lors du traitement d’un fichier.")
