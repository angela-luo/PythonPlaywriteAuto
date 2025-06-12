"""
File: utils/logger.py
Creator: Angel
Created: 2025-06-05
Description: Logger configuration and utilities
"""

import logging
import os
from datetime import datetime
from config.config import Config


def setup_logger(name, log_level=Config.LOG_LEVEL) -> logging.Logger:
    """ Configure and return a logger"""
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Create log directory
    os.makedirs(Config.LOG_DIR, exist_ok=True)

    # File handler
    timestamp = datetime.now().strftime("%Y%m%d")
    file_handler = logging.FileHandler(f"{Config.LOG_DIR}/{name}_{timestamp}.log")
    file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_format)
    file_handler.setLevel(log_level)

    # Console handler
    console_handler = logging.StreamHandler()
    console_format = logging.Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(console_format)
    console_handler.setLevel(log_level)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger