#!/bin/bash
set -e
# set environmental variables
condaEnvName=./env/
echo "Conda environment: $condaEnvName"
echo "  Update environement variables"

# Activate conda env
eval "$(conda shell.bash hook)"
conda activate $condaEnvName

# TODO: conda env config vars set needs to take effects before dotenv-flow-conda.sh call
conda env config vars set _ENV=$1

. ./scripts/dotenv-flow-conda.sh $1

# List conda env variables
conda deactivate
conda activate $condaEnvName
echo "Env variables:"
conda env config vars list
