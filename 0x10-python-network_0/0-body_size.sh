#!/bin/bash
#takes a URL, sends a request and displays size of the body of the response
curl -s "$1" | wc -c
