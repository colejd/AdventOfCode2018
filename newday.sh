#!/bin/bash

#DD=$(date +%d)
DD=$1

folder="day_$DD"

mkdir "$folder"
cp template.py "$folder/day$1part1.py"
cp template.py "$folder/day$1part2.py"
touch "$folder/input.txt"
