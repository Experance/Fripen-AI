#!/bin/bash

# by default nginx is dormant so we need to start it on each run
service nginx start

# get into the proper directory
cd /app

# run the app
gunicorn --config /app/config.py main:app
