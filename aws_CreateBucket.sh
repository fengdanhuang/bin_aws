#!/bin/bash

if [ $# -ne 2 ]; then
	echo
	echo "  Usage (General): "$0" bucket(new) region(new)"
	echo
	exit 1
fi


BUCKET=$1
REGION=$2


echo -e "\n===============================================================\n"
echo "  The program is:   "$0
echo "  The new S3 bucket is:   "$1
echo "  The new region is:   "$2
echo -e '\n'


echo "aws s3api create-bucket --bucket $BUCKET --region $REGION"
aws s3api create-bucket --bucket $BUCKET --region $REGION
echo -e '\n'
