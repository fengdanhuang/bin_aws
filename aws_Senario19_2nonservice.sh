


echo "================================================================="
echo "aws iam list-user-policies --output $OUTFORMAT --user-name $USER"
aws iam list-user-policies --output $OUTFORMAT --user-name $USER
echo -e '\n'

echo "================================================================="
echo "aws iam list-groups-for-user --output $OUTFORMAT --user-name $USER"
aws iam list-groups-for-user --output $OUTFORMAT --user-name $USER
echo -e '\n'

list-group-policies

get-group-policy

CreateDBSnapshot

CreateUser

AddUserToGroup
