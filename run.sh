#!/bin/bash
set -e
./install.sh
source venv/bin/activate
docker run -p 8000:8000 fastapi-orders
