#!/bin/bash


if [ $# -ne 0 ]; then
        echo
        echo "  Usage (General): "$0
        echo
        exit 1
fi


PROGRAM=$0


echo -e "\n===============================================================\n"
echo "  The program is:   "$PROGRAM
echo -e '\n'

echo "aws rds describe-db-snapshots"
aws rds describe-db-snapshots
echo -e '\n'

echo -e "\n===============================================================\n"
