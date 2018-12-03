#!/bin/bash

if [  $# -ne 1 ]; then
	echo "Usage: $0 day"
	exit 1
fi

day=$1
sessionid=`cat sessionid.txt`

mkdir -p "../Day$day"
curl --cookie "$sessionid" "https://adventofcode.com/2018/day/$day/input" > "../Day$day/input.txt"
