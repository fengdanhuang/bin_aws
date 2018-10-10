#!/bin/bash

SSH_USERNAME="ubuntu"
REMOTE_IP="10.50.41.157"
CASSANDRA_USERNAME="cassandra"
CASSANDRA_PASSWORD="cassandra"
#TENANTNAME=$1
TENANTNAME="KeyTech"
#APPNAME=$2
APPNAME="AWS"
#APPINSTNAME=$3
APPINSTNAME="AWS_Attack_Normal_Scenario"
EVNTDATE=`date -u '+%Y-%m-%d'` 	#return the UTC date
EVNTHOUR_S=`date -u '+%H'` 	#return the UTC hour
SLEEPTIME=300


echo "APPRITY_HOME = "$APPRITY_HOME
echo "APPRITY_SOURCE_HOME = "$APPRITY_SOURCE_HOME
echo "CASB_TESTS_HOME = "$CASB_TESTS_HOME
echo "SSH_USERNAME = "$SSH_USERNAME
echo "REMOTE_IP = "$REMOTE_IP
echo "CASSANDRA_USERNAME = "$CASSANDRA_USERNAME
echo "CASSANDRA_PASSWORD = "$CASSANDRA_PASSWORD
echo "TENANTNAME = "$TENANTNAME
echo "APPNAME = "$APPNAME
echo "APPINSTNAME = "$APPINSTNAME
echo "EVNTDATE = "$EVNTDATE
echo "EVNTHOUR_S = "$EVNTHOUR_S
echo "SLEEPTIME = "$SLEEPTIME


#Assume that the casb_tests repo has been built by the 
echo
echo "cd ~/github/casb-tests/ui_new/integ"
cd ~/github/casb-tests/ui_new/integ

#Generate Attack and Normal Scenarios
echo
echo "mvn clean test -Dtest=AWS_NormalScenarios#NormalSenario30"
mvn clean test -Dtest=AWS_NormalScenarios#NormalSenario30
echo "mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario30"
mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario30

#Register a AWS app instance on QA (RC) Stack
echo "mvn clean test -Dtest=AWS_RegisterInstance -e"
mvn clean test -Dtest=AWS_RegisterInstance -e


EVNTHOUR_E=`date -u '+%H'` 	#return the UTC hour
echo "EVNTHOUR_E = "$EVNTHOUR_E


echo
echo "ssh -t -F ~/Downloads/ssh.config $SSH_USERNAME@$REMOTE_IP 'python readActivityASCII.py -u $CASSANDRA_USERNAME -p $CASSANDRA_PASSWORD -tn $TENANTNAME -app $APPNAME -ait $APPINSTNAME -ed $EVNTDATE -eh $EVNTHOUR_S'"
ssh -F ~/Downloads/ssh.config $SSH_USERNAME@$REMOTE_IP <<EOF
python readActivityASCII.py -u cassandra -p $CASSANDRA_PASSWORD -tn $TENANTNAME -app $APPNAME -ait $APPINSTNAME -ed $EVNTDATE -eh $EVNTHOUR_E
EOF
