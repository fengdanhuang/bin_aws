#!/Applications/anaconda/bin/python
#owner: Chao Feng, cfeng@palerra.com
#sample run: python genHistograms.py csv_file Y

#import python lib:
import sys
import logging
import time
import datetime

#import Scipy lib:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

#import my classes:
from DSUtility.Code_Name import Code_Name


logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

if len(sys.argv)<3:
        print "\n  Usage: ProgramName CSV_file(1 file) Include_Zero(Y or N)"
        print
	exit(0)

Program=sys.argv[0]
Input_File=sys.argv[1]
Include_Zero=sys.argv[2]

#get the timestamp
ts = time.time()
dts = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d')
Elements = Input_File.split('.')[0].split('_') #Element[1]:App Name, Element[2]:Tenant Name

if Include_Zero == 'Y':
	Output_File = dts + "_" + Code_Name.TenantCode_Name[Elements[1]] + '_' + Elements[2] + '_Zero' 
else:
	Output_File = dts + "_" + Code_Name.TenantCode_Name[Elements[1]] + '_' + Elements[2] + '_NonZero'
#print Output_File

logging.info("The program is: %s", Program)
logging.info("The input .csv file is %s", Input_File)
logging.info("The output file is: %s", Output_File)

df = pd.read_csv(Input_File)

logging.info("df.index = %s", df.index)
logging.info("df.columns = %s", df.columns)
logging.info("df.describe() = %s", df.describe())


#get a subset of the data frame, still a data frame
#dfA = df.loc[:,['c001','c002','c003','c005','c006','c007','c011','c012','c017']]
dfA = df.loc[:,['c001','c002','c003','c005','c006','c007','c017']]

##print dfA
logging.info("dfA = %s", dfA)



columns = ['c001','c002','c003','c005','c006','c007','c017']
columns_Mean = {'c001':'# of login',
		'c002':'# of distinct login IP ',
		'c003':'# of distinct login location',
		'c005':'# of failed login',
		'c006':'# of distinct failed login IP',
		'c007':'# of distinct failed login location',
		'c017':'# of distinct IP2 for all actions'
		}


# the histogram of the data
fig = plt.figure("Histogram for login",figsize=(17,11),edgecolor='k')
i=1
for cx in columns:
	
	##print cx,":"
	logging.info("%s_Zero:",cx)
	cxArray = dfA[cx].values #csArray is 1D numpy array corresponding to 'c00x'
	logging.info("%s", cxArray)
	
	cxArrayNoZero = cxArray[cxArray!=np.array(0)] #remove all '0' from c00x array	
	logging.info("%s_None_Zero:",cx)
	logging.info("%s",cxArrayNoZero)
	
	plt.subplot(3,3,i)
	if Include_Zero == 'Y':
		logging.info("max = %s, min = %s, max-min = %s",cxArray.max(), cxArray.min(), cxArray.max()-cxArray.min())
		NOfBins = (cxArray.max() - cxArray.min())/1 #Set the length of bin = 1
	elif Include_Zero == 'N':
		logging.info("max = %s, min = %s, max-min = %s",cxArrayNoZero.max(), cxArrayNoZero.min(), cxArrayNoZero.max()-cxArrayNoZero.min())
		NOfBins = (cxArrayNoZero.max() - cxArrayNoZero.min())/1 #Set the length of bin = 1
	
	if NOfBins == 1:   	#When there is only one bin, we set # of bins as 2.
		NOfBins = 2	
	elif NOfBins == 0:	#When max == min, we should at least set up one bin
		NOfBins = 1	
	if Include_Zero == 'Y':
		cx_n, cx_bins, cx_patches = plt.hist(cxArray, bins=NOfBins, color='green')
	elif Include_Zero == 'N':
		cx_n, cx_bins, cx_patches = plt.hist(cxArrayNoZero, bins=NOfBins, color='green')
	plt.xlabel(columns_Mean[cx])
	plt.ylabel('Frequency')
	xint = []
	locs, labels = plt.xticks()
	for each in locs:
    		xint.append(int(each))
	plt.xticks(xint)
	plt.grid(True)
	plt.plot()
	i=i+1

figSuperTitle = 'Histograms for ' + Output_File
fig.suptitle(figSuperTitle, fontsize=14, fontweight='bold')

#plt.show()

pdfFileName = Output_File + '_Hist' + '.pdf'
pp = PdfPages(pdfFileName)	#Altenative: plt.savefig(pp, format='pdf')
pp.savefig()
#pp.savefig()
pp.close()
