#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept.
curl -s -i -X OPTIONS $1
