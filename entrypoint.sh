#!/bin/bash

if [ -f /project/target/bin/activate ]; then
	source /project/target/bin/activate
fi

python /opt/tests.py $@
