#!/bin/bash
# Returns a status code
curl -sLw "%{http_code}" "$1" -o /dev/null
