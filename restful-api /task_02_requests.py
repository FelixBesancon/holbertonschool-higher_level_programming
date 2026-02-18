#!/usr/bin/python3
"""
This module provides :
    fetch_and_print_posts function.
    fetch_and_save_posts function.
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts from an API and print their titles."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response_code = response.status_code
    print("Status Code: {}".format(response_code))
    if response_code == requests.codes.ok:
        posts = response.json()
        for element in posts:
            print(element["title"])


def fetch_and_save_posts():
    """
    Fetch posts from an API and saves their id, title and body
    in a csv file.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response_code = response.status_code
    if response_code == requests.codes.ok:
        data_list = []
        posts = response.json()
        for element in posts:
            data = {}
            data["id"] = element.get("id")
            data["title"] = element.get("title")
            data["body"] = element.get("body")
            data_list.append(data)
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            for csv_data in data_list:
                writer.writerow(csv_data)
