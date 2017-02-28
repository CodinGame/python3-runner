#!/bin/bash

cd /project/target

# Install pip dependencies
if [ -f requirements.txt ]; then
	pip install -r requirements.txt
fi
