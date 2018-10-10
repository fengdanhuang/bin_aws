#!/bin/bash


if [ $# -ne 2 ]; then
	echo
	echo "  Usage (General): "$0" trail(new) s3_bucket(existed)"
	echo
	exit 1
fi


TRAIL=$1
BUCKET=$2

echo -e "\n===============================================================\n"
echo "  The program is:   "$0
echo "  The new trail is:   "$1
echo "  The new S3 bucket is:   "$2
echo -e '\n'



echo "aws cloudtrail create-trail --name $TRAIL --s3-bucket-name $BUCKET"
aws cloudtrail create-trail --name $TRAIL --s3-bucket-name $BUCKET
echo -e '\n'

