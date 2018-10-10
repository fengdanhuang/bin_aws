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
#Test
#import my classes:
from DSUtility.Code_Name import Code_Name


logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

if len(sys.argv)<2:
        logging.info("\n  Usage: ProgramName CSV_file(1 file)")
        exit(0)

Program=sys.argv[0]
#accept 1th to nth parameters
i=1
Files=[]
while (i < len(sys.argv)):
        Files.append(sys.argv[i])
        i = i+1
FilesString = ' '.join(Files)

logging.info("The program is: %s", Program)
logging.info("The input files are %s\n\n", Files)


#get the timestamp
ts = time.time()
dts = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d')
Elements = Files[0].split('.')[0].split('_') #Element[1]:App Name, Element[2]:Tenant Name



#Output_File = dts + "_" + Code_Name.TenantCode_Name[Elements[1]] + '_' + Elements[2]
Output_File = 'BarChart_For_Threat'
#fileNameObj = genFileName(Files)
#Output_File = fileNameObj.Name
logging.info(Output_File)

fig = plt.figure("Bar chart for threats",figsize=(17,11),edgecolor='k')

dfALL = []
for file in Files:  #glob is used to read '*', '?' shell characters
        if file.endswith(".csv"):
                logging.info("file = %s\n",file)
                df = pd.read_csv(file)
                dfALL.append(df)
dfALL = pd.concat(dfALL)

pdfFileName = Output_File + '_threatsPerDay' + '.pdf'
pp = PdfPages(pdfFileName)      #Altenative: plt.savefig(pp, format='pdf')

logging.info("dfALL.index = %s", dfALL.index)
logging.info("dfALL.columns = %s", dfALL.columns)
logging.info("dfALL.describe() = %s", dfALL.describe())

#get a subset of the data frame, still a data frame
dfDateAttributes = dfALL.loc[:,['snapdate']]
logging.info("dfDateAttributes = %s", dfDateAttributes)
dfDateAttributes.groupby(by='snapdate').size().plot.bar()
plt.axhline(0, color='yellowgreen')
#plt.show()
pp.savefig()
pp.close()
