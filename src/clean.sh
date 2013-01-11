#!/bin/bash

rm -f *.aux
rm -f *.log

if [[ ! -d output ]]; then
	mkdir output
fi
mv *.toc output
mv *.pdf output
