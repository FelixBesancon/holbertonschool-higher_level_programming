#!/usr/bin/python3
"""
This module provides the function convert_csv_to_json,
that converts CSV to JSON.
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Deserializes the CSV file given, then serializes
    it into JSON file.
    Exception:
        Returns False if file not found.
    """
    try:
        with open(csv_filename, "r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            obj = list(reader)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(obj, json_file)

        return True

    except (FileNotFoundError, OSError, TypeError, csv.Error):
        return False
