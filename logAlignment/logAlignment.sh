#!/bin/bash

for inputFiles in $@; do
	python logScutch.py $inputFiles >> output.txt
done;

sort output.txt > outputSort.txt
