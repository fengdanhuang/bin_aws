#!/bin/bash

if [ $# -ne 2 ]; then
	echo
	echo "  Usage (General): "$0" trail(new) bucket(new)"
	echo
	exit 1
fi


TRAIL=$1
BUCKET=$2


echo -e "\n===============================================================\n"
echo "  The program is:   "$0
echo "  The new trail is:   "$1
echo "  The new S3 bucket is:   "$2

echo "aws cloudtrail create-subscription --name $TRAIL --s3-new-bucket $BUCKET"
aws cloudtrail create-subscription --name $TRAIL --s3-new-bucket $BUCKET
echo -e '\n'
