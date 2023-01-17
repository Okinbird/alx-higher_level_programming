#!/usr/bin/python3
"""script that takes in a letter and sends a POST request"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        info = {"q": argv[1]}
    else:
        info = {"q": ""}
    r = requests.post("http://0.0.0.0:5000/search_user", data=info)
    try:
        if r.json() == {}:
            print("No result")
        else:
            print("[{}] ".format(r.json().get("id")), end="")
            print(r.json().get("name"))
    except ValueError:
        print("Not a valid JSON")
