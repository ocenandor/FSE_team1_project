#!/bin/bash
mkdir build
cd build 
cmake ..
make
cd ../
cd python
./all-compile.sh