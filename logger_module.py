import logging
import os
<<<<<<< HEAD
from datetime import datetime

APPLICATION_LOG_DIR = "logs/application_logs"
EXCEPTION_LOG_DIR = "logs/exception_logs"

os.makedirs(APPLICATION_LOG_DIR, exist_ok=True)
os.makedirs(EXCEPTION_LOG_DIR, exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")

application_log_file = os.path.join(
    APPLICATION_LOG_DIR,
    f"{today}.log"
)

exception_log_file = os.path.join(
    EXCEPTION_LOG_DIR,
    f"{today}.log"
)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s",
    "%d-%m-%Y %H:%M:%S"
)

application_logger = logging.getLogger("ApplicationLogger")
application_logger.setLevel(logging.INFO)
application_logger.propagate = False

if not application_logger.handlers:

    app_handler = logging.FileHandler(
        application_log_file,
        encoding="utf-8"
    )

    app_handler.setFormatter(formatter)

    application_logger.addHandler(app_handler)

exception_logger = logging.getLogger("ExceptionLogger")
exception_logger.setLevel(logging.ERROR)
exception_logger.propagate = False

if not exception_logger.handlers:

    exception_handler = logging.FileHandler(
        exception_log_file,
        encoding="utf-8"
    )

    exception_handler.setFormatter(formatter)

    exception_logger.addHandler(exception_handler)

def log_application(message):
    application_logger.info(message)


def log_warning(message):
    application_logger.warning(message)


def log_debug(message):
    application_logger.debug(message)


def log_exception(message):
    exception_logger.error(message)


def log_critical(message):
    exception_logger.critical(message)
=======

# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logging
logging.basicConfig(
    filename="logs/healthcare.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S"
)

def log_info(message):
    """Log information messages."""
    logging.info(message)

def log_warning(message):
    """Log warning messages."""
    logging.warning(message)

def log_error(message):
    """Log error messages."""
    logging.error(message)

def log_critical(message):
    """Log critical messages."""
    logging.critical(message)

def log_debug(message):
    """Log debug messages."""
    logging.debug(message)

def log_exception(message):
    """Log exception messages."""
    logging.exception(message)
>>>>>>> db9a5911a3f9d82b30a94cf078ccae0b8f3dd91f
