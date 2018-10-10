#/!/bin/bash


for var in "$@"
do
    	echo "$var"
	genBarChart.py $var
	#genPieChart.py $var
done
