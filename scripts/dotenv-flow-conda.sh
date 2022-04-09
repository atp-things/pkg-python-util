#!/bin/bash
# Set environmental variables to conda environment.
####################################################

### Init
set -e

### Functions
function condaExportDotEnvFile () {

    local FILE=$1
    if [ -f "$FILE" ]; then
        echo "Load: $FILE"
        while read -r line || [ -n "$line" ];
        do
            conda env config vars set $line
        done < $FILE
    fi
}

### Input parameters
# Get the name of environment
# environmental variables
ENV=$NODE_ENV
ENV=$PY_ENV
ENV=$_ENV
# script parameters
ENV=$1
echo "Environment: $ENV"

### Main
# Load enviremental variables to conda environement from files from files
condaExportDotEnvFile .env
condaExportDotEnvFile .env.local
condaExportDotEnvFile .env.$ENV
condaExportDotEnvFile .env.$ENV.local
