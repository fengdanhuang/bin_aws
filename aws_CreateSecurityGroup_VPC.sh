#!/bin/bash

if [ $# -ne 3 ]; then
	echo
	echo "  Usage (General): "$0" security_group_name(new) description(new) VPC_id(existed)"
	echo
	exit 1
fi


GROUP_NAME=$1
DESCRIPTION=$2
VPC_ID=$3

echo -e "\n===============================================================\n"
echo "  The program is:   "$0
echo "  The description is:   "$1
echo "  The vpc id is:   "$2
echo -e '\n'


echo "aws ec2 create-security-group --group-name $GROUP_NAME --description $DESCRIPTION --vpc-id $VPC_ID"
aws ec2 create-security-group --group-name $GROUP_NAME --description $DESCRIPTION --vpc-id $VPC_ID
echo -e '\n'
