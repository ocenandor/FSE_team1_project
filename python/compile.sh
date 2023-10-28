#!/bin/bash

python3 setup.py build_ext --inplace
cp img_*.so img.py ../test/
