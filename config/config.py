"""
File: config/config.py
Creator: Angel
Created 2025-06-05
"""

import os


class Config:
    # Basic configuration
    BASE_URL = "https://petstore.octoperf.com"
    LOGIN_URL = "/actions/Account.action?signonForm="
    REGISTER_URL = "/actions/Account.action?newAccountForm="
    BROWSER = "chromium"  # Options: chromium, firefox, webkit
    HEADLESS = False  # Whether in headless mode
    TIMEOUT = 10000  # Timeout time (milliseconds)
    LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL

    # Path configuration
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Project root directory
    print(f"Base directory: {BASE_DIR}")
    LOG_DIR = os.path.join(BASE_DIR, 'reports', 'logs')
    SCREENSHOT_DIR = os.path.join(BASE_DIR, 'reports', 'screenshots')
    ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, 'reports', 'allure-results')
    print(f"Allure results directory: {ALLURE_RESULTS_DIR}")
    ALLURE_REPORT_DIR = os.path.join(BASE_DIR, 'reports', 'allure-report')
    # Add the path to the Allure executable file (modify according to your actual installation path)
    ALLURE_BIN_PATH = r"C:\Programs\allure-2.20.1\bin\allure.bat"  # Windows

    # Ensure the directory exists
    os.makedirs(LOG_DIR, exist_ok=True)
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    os.makedirs(ALLURE_RESULTS_DIR, exist_ok=True)
    os.makedirs(ALLURE_REPORT_DIR, exist_ok=True)