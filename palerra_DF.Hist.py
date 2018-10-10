#!/Applications/anaconda/bin/python

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import cluster

if len(sys.argv)<2:
        print "\n  Usage: ProgramName CSV_file"
        exit(0)

Program=sys.argv[0]
Input_File=sys.argv[1]

print " The program is: ", Program
print " The input .csv file is: ", Input_File

df = pd.read_csv(Input_File);

#print df;

print " df.intex = ", df.index;
print " df.columns = ", df.columns;
print " df.describe() = ";
print df.describe();

#print df['c001'].hist(by=df['tenantid'],grid=False,bins=10,layout=(2,2))
df['c001'].hist(by=df['appname'],bins=20)
df['c002'].hist(by=df['appname'],bins=10)
df['c003'].hist(by=df['appname'],bins=10)
df['c005'].hist(by=df['appname'],bins=10)
df['c006'].hist(by=df['appname'],bins=10)
df['c007'].hist(by=df['appname'],bins=10)
df['c011'].hist(by=df['appname'],bins=10)
df['c012'].hist(by=df['appname'],bins=10)
df['c017'].hist(by=df['appname'],bins=10)

#print df['c001'].hist(by=df['snapdate'])
#print df['c001'].hist(by=df['evntactor'])


plt.show()
