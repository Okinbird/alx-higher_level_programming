#!/usr/bin/python3
"""Script that takes in a URL and an email address"""
import requests
from sys import argv


if __name__ == "__main__":
    email = {'email': argv[2]}
    r = requests.post(argv[1], data=email)
    print(r.text)
