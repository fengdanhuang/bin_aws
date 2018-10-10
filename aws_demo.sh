#/!/bin/bash


OUTFORMAT=json
USER="LABChao"


echo "================================================================="
echo "aws configure list"
aws configure list
echo -e '\n'


echo "aws iam list-users --output $OUTFORMAT"
aws iam list-users --output $OUTFORMAT
echo -e '\n'


echo "aws iam list-groups --output $OUTFORMAT"
aws iam list-groups --output $OUTFORMAT
echo -e '\n'


echo "aws iam list-policies --output $OUTFORMAT"
aws iam list-policies --output $OUTFORMAT
echo -e '\n'


echo "aws iam list-roles --output $OUTFORMAT"
aws iam list-roles --output $OUTFORMAT
echo -e '\n'


echo "aws iam list-user-policies --output $OUTFORMAT --user-name $USER"
aws iam list-user-policies --output $OUTFORMAT --user-name $USER
echo -e '\n'


echo "aws iam list-groups-for-user --output $OUTFORMAT --user-name $USER"
aws iam list-groups-for-user --output $OUTFORMAT --user-name $USER
echo -e '\n'


echo "================================================================="


