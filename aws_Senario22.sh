#!/bin/bash


if [ $# -ne 3 ]; then
	echo
	echo "  Usage (General): "$0" security_group(existed) protocol port"
	echo
	exit 1
fi

GROUP_ID=$1
PROTOCOL=$2
PORT=$3


echo -e "\n===============================================================\n"
echo "  The program is:   "$0
echo "  The existed security group is:   "$1
echo "  The protocol is:   "$2
echo "  The port is:   "$3
echo -e '\n'


echo "aws ec2 authorize-security-group-ingress --group-id $GROUP_ID --protocol $PROTOCOL --port $PORT"
aws ec2 authorize-security-group-ingress --group-id $GROUP_ID --protocol $PROTOCOL --port $PORT
echo -e '\n'


echo "================================================================="
