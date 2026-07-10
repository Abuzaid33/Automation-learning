
import logging

logging.basicConfig(
    filename="Day-14/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log(message):
    logging.info(message)
    
logging.basicConfig(
    filename="Day-14/automation.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log(message):
    logging.warning(message)
    
logging.basicConfig(
    filename="Day-14/automation.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log(message):
    logging.error(message)
    
logging.basicConfig(
    filename="Day-14/automation.log",
    level=logging.CRITICAL,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def log(message):
    logging.critical(message)


