#!/bin/bash
apt update
apt install python3 python3-pip
apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
pip install -r requirements.txt --break-system-packages
