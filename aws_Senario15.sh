#!/bin/bash


if [ $# -ne 3 ]; then
        echo
        echo "  Usage (General): "$0" db-snapshot-identifier(new) db-instance-identifier(new) attribute-name(existed)"
        echo
        exit 1
fi


PROGRAM=$0
DB_SNAPSHOT_IDENTIFIER=$1
DB_INSTANCE_IDENTIFIER=$2
ATTRIBUTE_NAME=$3


echo -e "\n===============================================================\n"
echo "  The program is:   "$PROGRAM
echo "  The new db snapshot identifier is:   "$DB_SHAPSHOT_IDENTIFIER
echo "  The existed db instance identifier is:   "$DB_INSTANCE_IDENTIFER
echo "  The existed attribute name is:   "$ATTRIBUTE_NAME
echo -e '\n'


echo "aws rds create-db-snapshot --db-snapshot-identifier $DB_SNAPSHOT_IDENTIFIER --db-instance-identifier $DB_INSTANCE_IDENTIFIER"
aws rds create-db-snapshot --db-snapshot-identifier $DB_SNAPSHOT_IDENTIFIER --db-instance-identifier $DB_INSTANCE_IDENTIFIER
echo -e '\n'


sleep 200


echo "aws rds modify-db-snapshot-attribute --db-snapshot-identifier $DB_SNAPSHOT_IDENTIFIER --attribute-name $ATTRIBUTE_NAME --values-to-add"
aws rds modify-db-snapshot-attribute --db-snapshot-identifier $DB_SNAPSHOT_IDENTIFIER --attribute-name $ATTRIBUTE_NAME --values-to-add
echo -e '\n'


echo -e "\n===============================================================\n"


