#!/Applications/anaconda/bin/python
#owner: Chao Feng, cfeng@palerra.com
#sample run: python genHistograms.py csv_file

import sys
import os
import logging
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.backends.backend_pdf import PdfPages
from sklearn import cluster

if len(sys.argv)<2:
        logging.error("Usage: ProgramName Directory")
        exit(0)

Program=sys.argv[0]
Directory=sys.argv[1]

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

logging.info("The program is: %s", Program)
logging.info("The directory is %s", Directory)

dfALL = []
for file in os.listdir(Directory):
	if file.endswith(".csv"):
		df = pd.read_csv(Directory + "/" + file)
		dfALL.append(df)
dfALL = pd.concat(dfALL)

logging.info("dfALL.index = %s", dfALL.index)
logging.info("dfALL.columns = %s", dfALL.columns)
logging.info("dfALL.describe() = %s", dfALL.describe())


#get a subset of the data frame, still a data frame
dfA = dfALL.loc[:,['c001','c002','c003','c005','c006','c007','c017']]
logging.info("dfA = %s", dfA)


columns = ['c001','c002','c003','c005','c006','c007','c017'];
columns_Mean = {'c001':'# of login',
		'c002':'# of distinct login IP ',
		'c003':'# of distinct login location',
		'c005':'# of failed login',
		'c006':'# of distinct failed login IP',
		'c007':'# of distinct failed login location',
		'c017':'# of distinct IP2 for all actions'
		}

# the histogram of the data
pdfFileName = Directory + '_EachApp_allUsers_Hist' + '.pdf'
pp = PdfPages(pdfFileName)	#Altenative: plt.savefig(pp, format='pdf')
fig = plt.figure("Histogram for login",figsize=(17,11),edgecolor='k')
i=1
for cx in columns:
	
	logging.info("%s:",cx)
	cxArray = dfA[cx].values #csArray is 1D numpy array corresponding to 'c00x'
	logging.info("%s", cxArray)
	cxArrayNoZero = cxArray[cxArray!=np.array(0)] #remove all '0' from c00x array
	
	logging.info("%s_None_Zero:",cx)
	logging.info("%s",cxArrayNoZero)
	
	plt.subplot(3,3,i)
	logging.info("max = %s, min = %s, max-min = %s",cxArray.max(), cxArray.min(), cxArray.max()-cxArray.min())
	NOfBins = (cxArray.max() - cxArray.min())/1 #Set the length of bin = 1
#	logging.info("max = %s, min = %s, max-min = %s",cxArrayNoZero.max(), cxArrayNoZero.min(), cxArrayNoZero.max()-cxArrayNoZero.min())
#	NOfBins = (cxArrayNoZero.max() - cxArrayNoZero.min())/1 #Set the length of bin = 1
	if NOfBins == 1:   	#When there is only one bin, we set # of bins as 2.
		NOfBins = 2	
	elif NOfBins == 0:	#When max == min, we should at least set up one bin
		NOfBins = 1
	cx_n, cx_bins, cx_patches = plt.hist(cxArray, bins=NOfBins, color='green')
#	cx_n, cx_bins, cx_patches = plt.hist(cxArrayNoZero, bins=NOfBins, color='green')
	plt.xlabel(columns_Mean[cx])
	plt.ylabel('Frequency')
	xint = [] #make sure the x tick are integers.
	locs, labels = plt.xticks()
	for each in locs:
    		xint.append(int(each))
	plt.xticks(xint)
	plt.grid(True)
	plt.plot()
#	if i % 3 == 0:
#		pp.savefig()
	i=i+1
figSuperTitle = 'Histograms of ' + Directory + ' for all users'
fig.suptitle(figSuperTitle, fontsize=14, fontweight='bold')

#plt.show()

pp.savefig()
pp.close()
