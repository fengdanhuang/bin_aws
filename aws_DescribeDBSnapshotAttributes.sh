#!/bin/bash


if [ $# -ne 1 ]; then
        echo
        echo "  Usage (General): "$0" db-snapshot-identifer(existed)"
        echo
        exit 1
fi


PROGRAM=$0
DB_SNAPSHOT_IDENTIFIER=$1

echo -e "\n===============================================================\n"
echo "  The program is:   "$PROGRAM
echo "  The db snapshot identifier is:   "$DB_SNAPSHOT_IDENTIFIER
echo -e '\n'


echo "aws rds describe-db-snapshot-attributes --db-snapshot-identifier $DB_SNAPSHOT_IDENTIFIER"
aws rds describe-db-snapshot-attributes --db-snapshot-identifier $DB_SNAPSHOT_IDENTIFIER
echo -e '\n'



echo -e "\n===============================================================\n"
