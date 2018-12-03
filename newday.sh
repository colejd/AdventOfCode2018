#!/bin/bash

mkdir "day-$1"
cp template.py "day-$1/day$1part1.py"
cp template.py "day-$1/day$1part2.py"
touch "day-$1/input.txt"