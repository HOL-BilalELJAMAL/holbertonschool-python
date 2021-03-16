#!/bin/bash
# Bash script that sends a GET request to a URL and displays the body of the response
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
