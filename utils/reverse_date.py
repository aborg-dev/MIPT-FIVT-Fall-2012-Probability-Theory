#!/usr/bin/env python3

from os import listdir
import re

pattern = re.compile('\d\d\.\d\d\.\d\d\d\d\.tex')

outputFile = file('commands', 'w')

fileNames = listdir('../src')

for name in fileNames:
	if (name.find(".tex") == -1):
		continue

	if (not pattern.match(name)):
		continue

	parts = name.split('.')
	newName = parts[2] + '.' + parts[1] + '.' + parts[0] + '.' + parts[3]
	command = 'git mv ' + name + ' ' + newName + '\n'

	outputFile.write(command)

