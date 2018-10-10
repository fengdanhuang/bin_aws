#!/bin/bash



if [ $# -ne 5 ]; then
	echo
	echo "  Usage (General): "$0" security_group(existed) protocol port user(existed) group(existed)"
	echo
	exit 1
fi


GROUP_ID=$1
PROTOCOL=$2
PORT=$3
USER_A=$4
GROUP_A=$5

echo -e "\n===============================================================\n"
echo "  The program is:   "$0
echo "  The existed security group is:   "$1
echo "  The protocol is:   "$2
echo "  The port is:   "$3
echo "  The existed user is:   "$4
echo "  The existed group is:   "$5
echo -e '\n'


echo "aws ec2 authorize-security-group-ingress --group-id $GROUP_ID --protocol $PROTOCOL --port $PORT"
aws ec2 authorize-security-group-ingress --group-id $GROUP_ID --protocol $PROTOCOL --port $PORT
echo -e '\n'


echo "aws iam delete-user --user-name $USER_A"
aws iam delete-user --user-name $USER_A
echo -e '\n'


echo "aws iam remove-user-from-group --user-name $USER_A --group-name $GROUP_A"
aws iam remove-user-from-group --user-name $USER_A --group-name $GROUP_A
echo -e '\n'


echo "aws iam delete-login-profile --user-name $USER_A"
aws iam delete-login-profile --user-name $USER_A
echo -e '\n'

echo "================================================================="
