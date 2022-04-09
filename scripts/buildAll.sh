#!/bin/bash
set -e
# Build package release

# Conda - delete old local releases
rm -f ./build/noarch/*.tar.bz2
# Create conda release
conda build  ./conda.recipe/ -c pyviz --output-folder ./build
# Copy package to builds folder
cp ./build/noarch/*.tar.bz2 ./builds/
