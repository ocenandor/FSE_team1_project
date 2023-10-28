#!/bin/bash

mkdir -p "build"
rm -r build/* 2>/dev/null
rm img_*.cpp img_*.so 2>/dev/null
gcc -pthread -Wl,--sysroot=/ -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -fPIC -I.. -c lib_cython.cpp -o build/lib_cython.o -std=c++17
wait
./compile.sh
