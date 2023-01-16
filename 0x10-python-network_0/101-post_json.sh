#!/bin/bash
# A Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
