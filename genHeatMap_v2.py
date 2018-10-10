#!/Applications/anaconda/bin/python
#owner: Chao Feng, cfeng@palerra.com
#sample run: 

#import python lib:
import sys 
import logging

#import Scipy lib:
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
from matplotlib.backends.backend_pdf import PdfPages
#import matplotlib.colors as colors 


#import my classes:
from DSUtility.ProcArg import ProcArg
from DSUtility.PDFFileName import PDFFileName
from DSUtility.DataProc import DataProc
from DSUtility.Plots import Plots

#process input arguments and print
pa1 = ProcArg(sys.argv)
pa1.checkNOfArgs(2)
pa1.getFilesFromArgs()
pa1.printArgv()

#generate output file name
pdfFileName1 = PDFFileName(pa1.getFilesAttri())
Output_File = pdfFileName1.getPDFFileName('HeatMap') 
logging.info("The Output File Name is:%s", Output_File)


dp1 = DataProc()
dp1.getDataFromCSV(pa1.getFilesAttri())
#dp1.printDataProperties()
dp1.getDataMultiColumns(['tenantid','appname','appinstname','snapdate'])
dp1.printDataColumn()

#dp1.getDataColumnGroupSize(['snapdate','tenantid'])
dp1.getDataColumnGroupSize(['tenantid','appname','appinstname','snapdate'])
#dp1.printDataColumnGroupSize()




df = dp1.getDataColumnGroupAttri()
print "df = ", df
#print "df.index = ", df.index
#print "df.columns = ", df.columns
#print "df.values = ", df.values

df1 = df.reset_index(level=['tenantid','appname','appinstname','snapdate'])
#print df1
#df2 = pd.pivot_table(df1, index=['tenantid','appname','appinstname'],columns='snapdate')
df2 = pd.pivot_table(df1, index='snapdate', columns=['tenantid','appname','appinstname'])
#print df2
df3 = df2.fillna(0)
print df3
#print df3.index
#print df3.columns
#df4 = df3.tail(30)
df4 = df3.iloc[0:30,0:5]
print df4
print df4.index
#print df4.index[0]
print df4.columns
#print df4.columns[0]

column_dict={}
columnDictStr=''
for i in np.arange(len(df4.columns)):
	column_dict[i] = df4.columns[i]

columnDictStr = ''.join("%s:%r\n" % (key,val) for (key,val) in column_dict.iteritems())
print columnDictStr

'''
#print df.reset_index(level=['tenantid','appname','appinstname','snapdate']).pivot(index='snapdate', columns=['tenantid','appname','snapdate']).fillna(0)
#print df.pivot(index='snapdate', columns=['tenantid','appname','snapdate']).fillna(0)
#df1 = df.reset_index(level=['snapdate','tenantid']).pivot(index='tenantid', columns='snapdate').fillna(0)
'''


#fig = plt.figure("Bar chart for aggregates data",figsize=(70,8),edgecolor='k')
fig = plt.figure("Heatmap for aggregates data", figsize=(15,15),edgecolor='k')
#fig, ax = plt.subplots(figsize=(15,8))
#fig, ax = plt.subplots()
#ax.pcolor('add' did not contain a loop with signature matchingf4, edgecolors='black', alpha=0.8)
#plt.pcolor(df4, cmap=plt.cm.Blues, alpha=0.8)
#fig.canvas.manager.window.move(100,400)
pp = PdfPages(Output_File)

plt.pcolormesh(df4.T.values, edgecolors='black', linewidth=0, alpha=0.8)
plt.colorbar()
#xlabels = df4.index
#ax.set_xticklabels(df4.columns, minor=True)
#ax.set_yticklabels(df4.index, minor=True)
# rotate the
#plt.xticks(rotation=90)
plt.xlabel('date')
plt.xticks(np.arange(len(df4.index))+0.5,df4.index,rotation=90)
plt.ylabel('tenantid_appname_tenantinstid')
#plt.yticks(np.arange(len(df4.columns))+0.5,df4.columns)
plt.yticks(np.arange(len(df4.columns))+0.5,np.arange(len(df4.columns)))
plt.text(1, 5, columnDictStr, fontsize=14, fontweight='bold')
#plt.title(1, 0.5, column_dict, fontsize=14, fontweight='bold')
#plt.show()
#p1 = Plots(dp1.getDataColumnGroupAttri())
#p1.doBarChartPlot(Output_File)
pp.savefig()
pp.close()
