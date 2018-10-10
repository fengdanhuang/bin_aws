#!/bin/bash

if [ $# -ne 4 ]; then
	echo 
	echo "Usage: ScriptName ANALYTICS_IP TENANTNAME APPNAME APPINSTNAME"
	echo
	exit
fi

ANALYTICS_IP=$1
TENANTNAME=$2
APPNAME=$3
APPINSTNAME=$4
#ANALYTICS_IP="10.50.41.181"
#TENANTNAME="KeyTech"
#APPNAME="AWS"
#APPINSTNAME="AWS_Attack_Normal_Scenario"

SSH_USERNAME="ubuntu"
CASSANDRA_USERNAME="cassandra"
CASSANDRA_PASSWORD="cassandra"
EVNTDATE=`date -u '+%Y-%m-%d'` 	#return the UTC date
EVNTHOUR=`date -u '+%H'` 	#return the UTC hour


echo "SSH_USERNAME = "$SSH_USERNAME
echo "ANALYTICS_IP = "$ANALYTICS_IP
echo "CASSANDRA_USERNAME = "$CASSANDRA_USERNAME
echo "CASSANDRA_PASSWORD = "$CASSANDRA_PASSWORD
echo "TENANTNAME = "$TENANTNAME
echo "APPNAME = "$APPNAME
echo "APPINSTNAME = "$APPINSTNAME
echo "EVNTDATE = "$EVNTDATE
echo "EVNTHOUR = "$EVNTHOUR


#Note: inside the EOF flags are the commands which will run on the remote machine.
ssh -F ~/Downloads/ssh.config $SSH_USERNAME@$ANALYTICS_IP <<EOF
echo "python readActivityASCII.py -u cassandra -p $CASSANDRA_PASSWORD -tn $TENANTNAME -app $APPNAME -ait $APPINSTNAME -ed $EVNTDATE -eh $EVNTHOUR"
python readActivityASCII.py -u cassandra -p $CASSANDRA_PASSWORD -tn $TENANTNAME -app $APPNAME -ait $APPINSTNAME -ed $EVNTDATE -eh $EVNTHOUR
EOF
#python readActivityASCII.py -u cassandra -p cassandra -tn KeyTech -app AWS -ait AWS_Attack_Normal_Scenario -ed 2017-12-18 -eh 3
