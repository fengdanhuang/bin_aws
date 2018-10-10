#!/bin/bash

if [ $# -ne 3 ]; then
        echo
        echo "  Usage (Attach Senario 19): "$0" user(existed) group(existed) policy(existed)" 
        echo
        exit 1
fi

USER=$1
GROUP=$2
POLICY=$3


echo -e "\n===============================================================\n"
echo "	The program is:   "$0
echo "	The existed user is:   "$1
echo "	The existed group is:   "$2
echo "	The existed policy is:   "$3
echo -e '\n'


echo "aws iam list-user-policies --user-name $USER"
aws iam list-user-policies --user-name $USER
echo -e '\n'


echo "aws iam list-groups-for-user --user-name $USER"
aws iam list-groups-for-user --user-name $USER
echo -e '\n'


echo "aws iam list-group-policies --group-name $GROUP"
aws iam list-group-policies --group-name $GROUP
echo -e '\n'


echo "aws iam list-group-policies --group-name $GROUP"
aws iam list-group-policies --group-name $GROUP
echo -e '\n'


echo "aws iam list-group-policies --group-name $GROUP"
aws iam list-group-policies --group-name $GROUP
echo -e '\n'

echo "aws iam get-group-policy --group-name $GROUP --policy-name $POLICY"
aws iam get-group-policy --group-name $GROUP --policy-name $POLICY
echo -e '\n'

echo "aws iam get-group-policy --group-name $GROUP --policy-name $POLICY"
aws iam get-group-policy --group-name $GROUP --policy-name $POLICY
echo -e '\n'

echo "aws iam get-group-policy --group-name $GROUP --policy-name $POLICY"
aws iam get-group-policy --group-name $GROUP --policy-name $POLICY
echo -e '\n'

echo "aws iam get-group-policy --group-name $GROUP --policy-name $POLICY"
aws iam get-group-policy --group-name $GROUP --policy-name $POLICY
echo -e '\n'

echo "aws iam get-group-policy --group-name $GROUP --policy-name $POLICY"
aws iam get-group-policy --group-name $GROUP --policy-name $POLICY
echo -e '\n'


echo "aws iam get-group-policy --group-name $GROUP --policy-name $POLICY"
aws iam get-group-policy --group-name $GROUP --policy-name $POLICY
echo -e '\n'


