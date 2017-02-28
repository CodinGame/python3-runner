#!/bin/bash

cd /project/target

# Copy project to /project/target
cp -a /project/source/. /project/target

# Install pip dependencies
pip install -r requirements.txt
