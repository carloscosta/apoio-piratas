#!/bin/bash
pip install -r /app/requirements.txt
#python /app/apoio/manage.py migrate
exec $@
