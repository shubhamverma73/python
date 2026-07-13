import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logger():
    # Logs folder create karo agar exist nahi karta
    os.makedirs("logs", exist_ok=True)

    # Common log format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File Handler
    file_handler = RotatingFileHandler(
        "logs/app.log",
        maxBytes=1024 * 1024,   # 1 MB file size limit if exceeded, new file will be created
        backupCount=5 # Number of backup files to keep if exceeded than older files will be deleted
    )
    file_handler.setFormatter(formatter)

    # Root Logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Existing handlers remove karo
    logger.handlers.clear()

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

'''
%(asctime)s → Time
%(levelname)s → INFO / ERROR
%(name)s → Kis module ne log kiya
%(message)s → Actual message
'''