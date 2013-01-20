#!/usr/bin/env python3

from os import listdir
import re

pattern = re.compile('\d\d\d\d\.\d\d\.\d\d\.tex')

outputFile = file('input_commands', 'w')

fileNames = listdir('../src')

commands = []

for name in fileNames:
	if (name.find(".tex") == -1):
		continue

	if (not pattern.match(name)):
		continue

	command = '\input{' + name + '}\n'
	commands.append(command);


commands = sorted(commands)

for command in commands:
	outputFile.write(command)

outputFile.close()
