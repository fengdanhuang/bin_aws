#!/bin/bash

if [ $# -ne 1 ]; then
	echo
	echo "  Usage (General): "$0" cird-block"
	echo
	exit 1
fi

CIDR_BLOCK=$1


echo -e "\n===============================================================\n"
echo "  The program is:   "$0
echo "  The new CIDR block is:   "$1
echo -e '\n'


echo "aws ec2 create-vpc --cidr-block $CIDR_BLOCK"
aws ec2 create-vpc --cidr-block $CIDR_BLOCK
echo -e '\n'

