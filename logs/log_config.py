import logging
import os
from datetime import datetime

# ----------------------------------------------------
# Create Log Directories
# ----------------------------------------------------

BASE_LOG_DIR = "logs"

APPLICATION_LOG_DIR = os.path.join(BASE_LOG_DIR, "application_logs")
EXCEPTION_LOG_DIR = os.path.join(BASE_LOG_DIR, "exception_logs")

os.makedirs(APPLICATION_LOG_DIR, exist_ok=True)
os.makedirs(EXCEPTION_LOG_DIR, exist_ok=True)

# ----------------------------------------------------
# Today's Log File
# ----------------------------------------------------

today = datetime.now().strftime("%Y-%m-%d")

application_log_file = os.path.join(
    APPLICATION_LOG_DIR,
    f"{today}.log"
)

exception_log_file = os.path.join(
    EXCEPTION_LOG_DIR,
    f"{today}.log"
)

# ----------------------------------------------------
# Formatter
# ----------------------------------------------------

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s",
    "%d-%m-%Y %H:%M:%S"
)

# ----------------------------------------------------
# Application Logger
# ----------------------------------------------------

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

# ----------------------------------------------------
# Exception Logger
# ----------------------------------------------------

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