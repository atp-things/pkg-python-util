#!/bin/bash
# Sphinix documentation - build

# Activate conda env
eval "$(conda shell.bash hook)"
conda activate ./env/

# Sphinex build static website
cd ./sphinx || exit
make html
cd .. || exit

# Getting Docusaurus deps
cd website || exit
npm install
cd .. || exit

# Parsing Sphinx docs and moving to Docusaurus

mkdir -p "website/pages/api/"
cwd=$(pwd)
python scripts/parse_sphinx.py -i "${cwd}/sphinx/build/html/" -o "${cwd}/website/pages/api/"

SPHINX_JS_DIR='sphinx/build/html/_static/'
DOCUSAURUS_JS_DIR='website/static/js/'

mkdir -p $DOCUSAURUS_JS_DIR

# move JS files from /sphinx/build/html/_static/*:
cp "${SPHINX_JS_DIR}documentation_options.js" "${DOCUSAURUS_JS_DIR}documentation_options.js"
cp "${SPHINX_JS_DIR}jquery.js" "${DOCUSAURUS_JS_DIR}jquery.js"
cp "${SPHINX_JS_DIR}underscore.js" "${DOCUSAURUS_JS_DIR}underscore.js"
cp "${SPHINX_JS_DIR}doctools.js" "${DOCUSAURUS_JS_DIR}doctools.js"
cp "${SPHINX_JS_DIR}language_data.js" "${DOCUSAURUS_JS_DIR}language_data.js"
cp "${SPHINX_JS_DIR}searchtools.js" "${DOCUSAURUS_JS_DIR}searchtools.js"

# searchindex.js is not static util
cp "sphinx/build/html/searchindex.js" "${DOCUSAURUS_JS_DIR}searchindex.js"

# copy module sources
cp -r "sphinx/build/html/_sources/" "website/static/_sphinx-sources/"


# Docusaurus develop
cd website || exit
npm start
cd .. || exit