#!/bin/bash

SSH_USERNAME="ubuntu"
REMOTE_IP="10.50.41.181"
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
echo "mvn clean test -Dtest=AWS_NormalScenarios#NormalSenario28"
mvn clean test -Dtest=AWS_NormalScenarios#NormalSenario28

:<<BLOCK
echo "mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario28"
mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario28
echo "mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario34"
mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario34
echo "mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario35"
mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario35
echo "mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario01"
mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario01
echo "mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario07"
mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario07
echo "mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario12"
mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario12
echo "mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario15"
mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario15
echo "mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario18"
mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario18
echo "mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario19"
mvn clean test -Dtest=AWS_AttackScenerioEventGenerator#AttackSenario19
BLOCK

#Register a AWS app instance on QA (RC) Stack
echo "mvn clean test -Dtest=AWS_RegisterInstance -e"
mvn clean test -Dtest=AWS_RegisterInstance -e

:<<BLOCK
echo
echo "sleep $SLEEPTIME"
#sleep $SLEEPTIME
#Count down seconds
echo "Start counting down ..."
secs=$SLEEPTIME
while [ $secs -gt 0 ]; do
   echo -ne "$secs\033[0K\r"
   sleep 1
   : $((secs--))
done
echo
BLOCK

EVNTHOUR_E=`date -u '+%H'` 	#return the UTC hour
echo "EVNTHOUR_E = "$EVNTHOUR_E


echo
echo "ssh -t -F ~/Downloads/ssh.config $SSH_USERNAME@$REMOTE_IP 'python readActivityASCII.py -u $CASSANDRA_USERNAME -p $CASSANDRA_PASSWORD -tn $TENANTNAME -app $APPNAME -ait $APPINSTNAME -ed $EVNTDATE -eh $EVNTHOUR_S'"
#ssh -F ~/Downloads/ssh.config $SSH_USERNAME@$REMOTE_IP 'python readActivityASCII.py -u $CASSANDRA_USERNAME -p $CASSANDRA_PASSWORD -tn $TENANTNAME -app $APPNAME -ait $APPINSTNAME -ed $EVNTDATE -eh $EVNTHOUR_S'
ssh -F ~/Downloads/ssh.config $SSH_USERNAME@$REMOTE_IP <<EOF
python readActivityASCII.py -u cassandra -p $CASSANDRA_PASSWORD -tn $TENANTNAME -app $APPNAME -ait $APPINSTNAME -ed $EVNTDATE -eh $EVNTHOUR_E
:<<BLOCK
for ((H=$EVNTHOUR_S; H<=$EVNTHOUR_E; H++))
do
	python readActivityASCII.py -u cassandra -p $CASSANDRA_PASSWORD -tn $TENANTNAME -app $APPNAME -ait $APPINSTNAME -ed $EVNTDATE -eh $H
	#python readActivityASCII.py -u cassandra -p $CASSANDRA_PASSWORD -tn $TENANTNAME -app $APPNAME -ait $APPINSTNAME -ed $EVNTDATE -eh $EVNTHOUR_S
done
BLOCK
EOF
#python readActivityASCII.py -u cassandra -p cassandra -tn KeyTech -app AWS -ait AWS_Attack_Normal_Scenario -ed 2017-12-18 -eh 3
