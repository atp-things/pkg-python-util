#!/bin/bash
# Sphinix build documentation

eval "$(conda shell.bash hook)"
conda activate ./env/
cd ./sphinx
make html