FROM ubuntu:23.04

WORKDIR /app

RUN apt-get update
RUN apt-get -y install git
RUN apt install python3 python3-pip -y
RUN apt install vim -y
RUN apt install cmake -y
RUN apt install clang g++ -y
RUN apt install dos2unix -y
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY . /app
RUN pip install -r ./requirements.txt --break-system-packages

RUN mkdir /build 

WORKDIR /app/build
RUN cmake ..
RUN make

WORKDIR /app/python
RUN dos2unix all-compile.sh
RUN dos2unix compile.sh
RUN ./all-compile.sh

WORKDIR /app/src
CMD python3 digit_predictor.py
