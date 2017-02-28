#!/bin/bash

cd /project/target

# Copy answer to the project
cp -r /project/answer/* /project/target/

# Run unit tests
python -m unittest $@
