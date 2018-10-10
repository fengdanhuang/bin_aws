#!/bin/bash


if [ $# -ne 1 ]; then
	echo
	echo "  Usage (General): "$0" trail(existed)"
	echo
	exit 1
fi


TRAIL=$1

echo -e "\n===============================================================\n"
echo "  The program is:   "$0
echo "  The existed trail is:   "$1
echo -e '\n'

echo "aws cloudtrail delete-trail --name $TRAIL"
aws cloudtrail delete-trail --name $TRAIL
echo -e '\n'
