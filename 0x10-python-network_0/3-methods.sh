#!/bin/bash
# Retrieves permissions
curl -sI "$1" | grep Allow | cut -d ' ' -f 2-
