#!/bin/bash
set -e
apt-get update && apt-get install -y python3 python3-pip python3-venv docker.io
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
docker build -t fastapi-orders .
