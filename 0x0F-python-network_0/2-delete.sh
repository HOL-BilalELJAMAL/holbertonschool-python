#!/bin/bash
# Bash script that sends a DELETE request to the URL passed and displays the body of the response
curl -s -X DELETE "$1"
