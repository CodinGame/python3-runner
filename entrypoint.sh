#!/bin/bash

if [ -f /project/target/bin/activate ]; then
	source /project/target/bin/activate
fi

cp -r /project/answer/* /project/target/
cd /project/target

python -m unittest $@
