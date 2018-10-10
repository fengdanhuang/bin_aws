#!/Applications/anaconda/bin/python
#owner: Chao Feng, cfeng@palerra.com
#sample run: python genHistograms.py csv_file


import sys
import os
import logging
from random import shuffle

#import Scipy lib:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.backends.backend_pdf import PdfPages

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

if len(sys.argv)<2:
        logging.info("\n	Usage: ProgramName Directory")
        exit(0)

Program=sys.argv[0]
Directory=sys.argv[1]


logging.info("The program is: %s", Program)
logging.info("The directory is %s", Directory)



dfALL = []
for file in os.listdir(Directory):
	if file.endswith(".csv"):
        	#print(file)
		df = pd.read_csv(Directory + "/" + file)
		dfALL.append(df)
dfALL = pd.concat(dfALL)

print dfALL;
#logging.info("dfAA = %s", dfALL)
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
#print x.__len__()
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
pdfFileName = Directory + '_AllUserAllApp_Pie' + '.pdf'
pp = PdfPages(pdfFileName)	#Altenative: plt.savefig(pp, format='pdf')

fig = plt.figure("Pie Chart for threats",figsize=(17,11),edgecolor='k')

figSuperTitle = 'The Pie Chart for all users and all apps'
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


