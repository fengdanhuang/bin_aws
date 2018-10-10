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

#plt.figure(1)
#plt.title('Histogram with tenant id')
#plt.subplot(331)
print df['c001'].hist(by=df['tenantid'],grid=False,bins=7,layout=(2,2))
#print df['c002'].hist(by=df['tenantid'],grid=False,bins=7,layout=(2,2))
#print df['c001'].hist(by=df['appname']
#print df['c001'].hist(by=df['snapdate'])
#print df['c001'].hist(by=df['evntactor'])

dfA = df.loc[:,['c001','c002','c003','c005','c006','c007','c011','c012','c017']]
print dfA

dfA.plot(kind='hist', title='Histogram', subplots=True, layout=(3,3), sharex=False)

fig, axes = plt.subplots(nrows=3, ncols=3)
df['c001'].plot(ax=axes[0,0]); axes[0,0].set_title('c001');




'''
#plt.subplot(332)
#print df['c002'].hist(by=df['tenantid'])
#plt.subplot(333)
#print df['c003'].hist(by=df['tenantid'])
#plt.subplot(334)
#print df['c005'].hist(by=df['tenantid'])
#plt.subplot(335)
#print df['c006'].hist(by=df['tenantid'])
#plt.subplot(336)
#print df['c007'].hist(by=df['tenantid'])
#plt.subplot(337)
print df['c011'].hist(by=df['tenantid'])
#plt.subplot(338)
print df['c012'].hist(by=df['tenantid'])
#plt.subplot(339)
print df['c017'].hist(by=df['tenantid'])
'''

#print df['c002'].hist(by=df['appname'])


plt.show()
