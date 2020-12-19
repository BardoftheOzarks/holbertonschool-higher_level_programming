#!/bin/bash
# Sends a request and displays the status code
curl -sLw "%{http_code}" "$1" -o /dev/null
