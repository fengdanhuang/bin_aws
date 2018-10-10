#!/bin/bash


if [ $# -ne 6 ]; then
	echo
	echo "  Usage (General): "$0" db_instance_identifier(new) allocate_storage(new) db_instance_class(new) engine master_username(new) master_user_password(new)"
	echo
	exit 1
fi



DB_INSTANCE_IDENTIFIER=$1
ALLOCATE_STORAGE=$2
DB_INSTANCE_CLASS=$3
ENGINE=$4
MASTER_USERNAME=$5
MASTER_USER_PASSWORD=$6


echo -e "\n===============================================================\n"
echo "  The program is:   "$0
echo "  The db instance identifier is:   "$1
echo "  The allocated storage is:   "$2
echo "  The db instancd class is:   "$3
echo "  The engine is:   "$4
echo "  The master username is:   "$5
echo "  The master user password is:   "$6
echo -e '\n'


echo "aws rds create-db-instance --db-instance-identifier $DB_INSTANCE_IDENTIFIER --allocated-storage $ALLOCATE_STORAGE --db-instance-class $DB_INSTANCE_CLASS --engine $ENGINE --master-username $MASTER_USERNAME --master-user-password $MASTER_USER_PASSWORD"
aws rds create-db-instance --db-instance-identifier $DB_INSTANCE_IDENTIFIER --allocated-storage $ALLOCATE_STORAGE --db-instance-class $DB_INSTANCE_CLASS --engine $ENGINE --master-username $MASTER_USERNAME --master-user-password $MASTER_USER_PASSWORD
echo -e '\n'
