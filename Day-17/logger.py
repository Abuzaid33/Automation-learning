import logging

logging.basicConfig(
    filename="Day-17/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log(message):
    logging.info(message)