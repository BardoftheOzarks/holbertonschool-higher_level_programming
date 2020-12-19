#!/bin/bash
# a bash script to retrieve the body length of a URL
curl -sI '$1' | grep Content-Length | cut -d ' ' -f 2
