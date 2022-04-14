#!/bin/bash
set -e
# Sphinix documentation - build

# Activate env
source .venv/bin/activate

# Sphinx build static website
cd ./sphinx || exit
make clean
make html
cd .. || exit
