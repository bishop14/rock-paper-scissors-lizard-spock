#!/bin/bash
set -ev

PACKAGE_NAME=function.zip
SITE_PATH=`python -c 'import sys; print(sys.path[2])'`

echo "Building Lambda package ${PACKAGE_NAME}"

rm function.zip || true

cd ${SITE_PATH}/site-packages

echo "Adding dependencies to package"
zip -r9 ${OLDPWD}/function.zip .
cd ${OLDPWD}

echo "Adding project modules to package"
zip -gr function.zip skill

echo "Adding lmabda function to package"
zip -g function.zip lambda_function.py

echo "Successfully created Lambda package at ${PWD}/${PACKAGE_NAME}"
echo "Completed."