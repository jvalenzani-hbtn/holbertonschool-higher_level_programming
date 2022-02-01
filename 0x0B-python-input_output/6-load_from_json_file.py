#!/usr/bin/python3
"""Load from JSON file"""

import json

def load_from_json_file(filename):
    """Load from JSON file"""
    with open(filename, "r") as f:
        try:
            return(json.load(f))
        except Exception as e:
            raise e
