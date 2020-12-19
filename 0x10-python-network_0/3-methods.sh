#!/bin/bash
# a bash script to retrieve permissions of a URL
curl -sI '$1' | grep Allow | cut -d ' ' -f 2-
