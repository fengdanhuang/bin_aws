#/!/bin/bash

if [ $# -ne 3 ]; then
	echo
	echo "	Usage (Attach Senario 30): "$0" user(new) group(existed) password(new)" 
	echo
	exit 1
fi


USER=$1
GROUP=$2
PASSWORD=$3

echo -e "\n===============================================================\n"
echo "  The program is:      "$0
echo "	The USER is:	"$1
echo "	The existed group is: "$2
echo "	The password is: "$4
echo -e '\n'


echo "aws iam create-user --user-name $USER"
aws iam create-user --user-name $USER
echo -e '\n'


echo "aws iam add-user-to-group --user-name $USER --group-name $GROUP"
aws iam add-user-to-group --user-name $USER --group-name $GROUP
echo -e '\n'


echo "aws iam create-login-profile --user-name $USER --password $PASSWORD"
aws iam create-login-profile --user-name $USER --password $PASSWORD
echo -e '\n'


echo "aws iam create-access-key --user $USER"
aws iam create-access-key --user-name $USER
echo -e '\n'
