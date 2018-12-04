#!/bin/bash

## https://stackoverflow.com/questions/59895/getting-the-source-directory-of-a-bash-script-from-within
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null && pwd )"

echo $DIR

if [  $# -ne 1 ]; then
	echo "Usage: $0 day"
	exit 1
fi

day=$1
sessionid=`cat $DIR/sessionid.txt`

mkdir -p "$DIR/../Day$day"
curl --cookie "$sessionid" "https://adventofcode.com/2018/day/$day/input" > "$DIR/../Day$day/input.txt"
