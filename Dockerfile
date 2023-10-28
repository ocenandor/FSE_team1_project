FROM ubuntu:23.04

RUN apt-get update
RUN apt-get -y install git
RUN apt install python3 python3-pip -y
RUN apt install vim -y
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
COPY . /app
RUN pip install -r app/requirements.txt --break-system-packages
WORKDIR /app
CMD python3 kamil_predictor.py
