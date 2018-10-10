#!/Applications/anaconda/bin/python
#owner: Chao Feng, cfeng@palerra.com
#sample run: python genHistograms.py csv_file

#import python lib:
import sys
import os
import glob
import time
import datetime
import logging
from random import shuffle

#import Scipy lib:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

#import my classes:
from DSUtility.Code_Name import Code_Name
from DSUtility.PDFFileName import PDFFileName

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

if len(sys.argv)<2:
        logging.info("\n	Usage: ProgramName Files")
        exit(0)

Program=sys.argv[0]
#accept 1th to nth parameters
i=1
Files=[]
while (i < len(sys.argv)):
	Files.append(sys.argv[i])
	i = i+1
FilesString = ' '.join(Files)
#logging.info("Files = %s", Files)
#logging.info("FilesString = %s", FilesString)



logging.info("The program is: %s", Program)
logging.info("The input files are %s\n\n", Files)

#get the timestamp
ts = time.time()
dts = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d')
Elements = Files[0].split('.')[0].split('_') #Element[1]:App Name, Element[2]:Tenant Name
#set a dictionary with the tenant code and its name:
 
#Output_File = dts + "_" + Code_Name.TenantCode_Name[Elements[1]] + '_' + Elements[2]
Output_File = dts + '_PieChart_' + Elements[2]
#fileNameObj = genFileName(Files)
#Output_File = fileNameObj.Name
logging.info("Output_File = ", Output_File)



dfALL = []
for file in Files:  #glob is used to read '*', '?' shell characters
	if file.endswith(".csv"):
		logging.info("file = %s\n",file)
		df = pd.read_csv(file)
		dfALL.append(df)
dfALL = pd.concat(dfALL)

#logging.info("dfALL = %s", dfALL)
logging.info("dfALL.index = %s", dfALL.index)
logging.info("dfALL.columns = %s", dfALL.columns)
logging.info("dfALL.describe() = %s", dfALL.describe())


#get a subset of the data frame, still a data frame
dfDateAttributes = dfALL.loc[:,['snapdate','attributes']]
logging.info("dfDateAttributes = %s", dfDateAttributes)

dataAttri = dfDateAttributes.values[:,1]
logging.info("	dataAttri = %s", dataAttri)
logging.info("	dataAttri.shape = %s", dataAttri.shape)
logging.info("	dataAttri.size = %s", dataAttri.size)
#logging.info("	dataAttri.dtype.name = %s", dataAttri.dtype.name)
print dataAttri.dtype.name
print dataAttri[0]
line = dataAttri[0].strip("{}").split(',')
print line
print "line.length = ", line.__len__()

x = []
i=0
while (i<dataAttri.size):	
	line = dataAttri[i].strip("{}").split(',')
	j = 0
	while (j<line.__len__()):
		if 'RiskAlertCode' in line[j]:
			x.append(line[j].split(':')[1])
		j = j+1

	i = i+1
#print x[6552]
logging.info("	x.__len__() = %s", x.__len__())

RiskCode = list(set(x))
print RiskCode
RiskCode_Dict = {}
for key in RiskCode:
	RiskCode_Dict[key] = 0
	for i in range(0, x.__len__()):
		if (x[i] == key): 
			RiskCode_Dict[key] = RiskCode_Dict[key] + 1
			
logging.info("RiskCode_Dict = %s", RiskCode_Dict)
logging.info("RiskCode_Dict.keys() = %s", RiskCode_Dict.keys())
logging.info("RiskCode_Dict.values() = %s", RiskCode_Dict.values())
logging.info("RiskCode_Dict.items() = %s", RiskCode_Dict.items())
	
# the pie chart of the data
pdfFileName = Output_File + '_Pie' + '.pdf'
pp = PdfPages(pdfFileName)	#Altenative: plt.savefig(pp, format='pdf')

fig = plt.figure("Pie Chart for threats",figsize=(17,11),edgecolor='k')

#figSuperTitle = 'Pie Chart of ' + Code_Name.TenantCode_Name[Elements[1]] + ' for all apps.'
figSuperTitle = 'Pie Chart of ' + Elements[1] + ' for all apps.'
fig.suptitle(figSuperTitle, fontsize=14, fontweight='bold')

Title = 'Total # of risks: ' + str(dataAttri.size)
#plt.title(Title)
plt.text(1, 0.5, Title, fontsize=14, fontweight='bold')
#colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
slices = [1,2,3] * 4 + [20, 25, 30] * 2
shuffle(slices)
cmap = plt.cm.prism
colors = cmap(np.linspace(0., 1., len(slices)))
patches, texts, autotexts = plt.pie(x=RiskCode_Dict.values(), labels=RiskCode_Dict.keys(), colors=colors, 
				    autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')

plt.legend(labels=RiskCode_Dict.items(), loc="upper right")

#plt.show()

pp.savefig()
pp.close()
