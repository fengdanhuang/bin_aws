#!/bin/bash

if [ $# -ne 1 ]; then
	echo -e "\n"
        echo "usage: shell_script_name No."
        echo -e "\n"
	echo "  script No. choice:"     
        echo "          1. show"
        echo "          2. describe"
        echo "          3. create table"
        echo "          4. copy [data] from [file]"
	echo "		5. drop [table]"
        echo -e "\n"
	exit 1
fi

Num=$1


case $Num in
	1)
		echo "cql---show version   :"
		cqlsh -e "show version"
		echo "cql---show clusters   :"
		cqlsh -e "show clusters"
		;;
	2)
		echo "cql---describe keyspaces	:"
		cqlsh -e "describe keyspaces"
		#echo "describe tables"
		#cqlsh -e "describe tables"
		;;
	3)
		echo "cql---create [table]	:" 
		cqlsh -e "create table apprity_core_schema_keyspace.threat_test (  
			tenantid text,
			applicationname text,
			appinstid text,
			snapdate text,
			runid text,
			rowid text,
			attributes text,
			category text,
			evnttime bigint,
			prediction text,
			userid text,
			priority text,
			status text,
			primary key (tenantid, applicationname, appinstid)
			)"
		;;
	4)
		echo "cql---copy [table] from [file]	:"
		cqlsh -e "copy apprity_core_schema_keyspace.threat_test (
				tenantid, 
				applicationname, 
				appinstid, 
				snapdate, 
				attributes, 
				category, 
				evnttime, 
				prediction, 
				priority, 
				rowid, 
				runid, 
				status, 
				userid
				) from '/Users/chaofeng/PalerraData/Threats/threats_lI7UU3Oo_AWS_Hub.csv' "	
		;;
	5)
		echo "cql---drop [table]	:"
		cqlsh -e "drop threat_test2"
		;;
	*)
		exit 1
esac	
