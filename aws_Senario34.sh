#!/bin/bash

if [ $# -ne 6 ]; then
        echo
        echo "  Usage (Attach Senario 34): "$0" user1(existed) user2(existed) user3(existed) user4(existed) group1(existed) group2(existed)" 
        echo
        exit 1
fi


USER_A=$1
USER_B=$2
USER_C=$3
USER_D=$4
GROUP_A=$5
GROUP_B=$6


echo -e "\n===============================================================\n"
echo "  The program is:      "$0
echo "  The existed user1 is: "$1
echo "  The existed user2 is: "$2
echo "  The existed user3 is: "$3
echo "  The existed user4 is: "$4
echo "  The existed group1 is: "$5
echo "  The existed group2 is: "$5
echo -e '\n'


echo "aws iam add-user-to-group --user-name $USER_A --group-name $GROUP_B"
aws iam add-user-to-group --user-name $USER_A --group-name $GROUP_B
echo -e '\n'


echo "aws iam add-user-to-group --user-name $USER_B --group-name $GROUP_B"
aws iam add-user-to-group --user-name $USER_B --group-name $GROUP_B
echo -e '\n'


echo "aws iam add-user-to-group --user-name $USER_C --group-name $GROUP_B"
aws iam add-user-to-group --user-name $USER_C --group-name $GROUP_B
echo -e '\n'


echo "aws iam add-user-to-group --user-name $USER_D --group-name $GROUP_B"
aws iam add-user-to-group --user-name $USER_D --group-name $GROUP_B
echo -e '\n'


echo "aws iam remove-user-from-group --user-name $USER_A --group-name $GROUP_A"
aws iam remove-user-from-group --user-name $USER_A --group-name $GROUP_A
echo -e '\n'


echo "aws iam remove-user-from-group --user-name $USER_B --group-name $GROUP_A"
aws iam remove-user-from-group --user-name $USER_B --group-name $GROUP_A
echo -e '\n'


echo "aws iam remove-user-from-group --user-name $USER_C --group-name $GROUP_A"
aws iam remove-user-from-group --user-name $USER_C --group-name $GROUP_A
echo -e '\n'


echo "aws iam remove-user-from-group --user-name $USER_D --group-name $GROUP_A"
aws iam remove-user-from-group --user-name $USER_D --group-name $GROUP_A
echo -e '\n'




