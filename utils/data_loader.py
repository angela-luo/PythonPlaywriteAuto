"""
File: utils/data_loader.py
Creator: Angel
Created: 2025-06-05
Description: Utility for loading test data from YAML files
"""

import yaml
import os

def load_test_data(file_name):
    """Load test data from YAML file"""
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)
    with open(file_path, 'r', encoding='utf-8') as file: # Explicit UTF-8 encoding
        return yaml.safe_load(file)