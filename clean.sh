#!/bin/bash

rm -f *.aux
rm -f *.log
rm -f *.toc

if [[ ! -d output ]]; then
	mkdir output
fi
mv *.pdf output
