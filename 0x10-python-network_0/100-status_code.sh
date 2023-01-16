#!/bin/bash
# Sends a GET request to a given URL and display the response status code.
curl -so /dev/null --write-out "%{http_code}" "$1"
