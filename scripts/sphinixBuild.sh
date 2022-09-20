#!/bin/bash
set -e
# Sphinix documentation - build

# Sphinx build static website
cd ./sphinx || exit
pipenv run make clean
pipenv run make html
cd .. || exit
