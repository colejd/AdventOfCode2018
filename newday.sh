#!/bin/bash

folder="day_$1"

mkdir "$folder"
cp template.py "$folder/day$1part1.py"
cp template.py "$folder/day$1part2.py"
touch "$folder/input.txt"
