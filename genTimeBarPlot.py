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
from DSPalerra.Code_Name import Code_Name


logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

if len(sys.argv)<2:
        logging.info("\n  Usage: ProgramName CSV_file(1 file)")
        exit(0)

Program=sys.argv[0]
Input_File=sys.argv[1]

#get the timestamp
ts = time.time()
dts = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d')
Elements = Input_File.split('.')[0].split('_') #Element[1]:App Name, Element[2]:Tenant Name


Output_File = dts + "_" + Code_Name.TenantCode_Name[Elements[1]] + '_' + Elements[2]
#fileNameObj = genFileName(Files)
#Output_File = fileNameObj.Name
logging.info(Output_File)


logging.info("The program is: %s", Program)
logging.info("The input .csv file is %s", Input_File)
logging.info("The output file is: %s", Output_File)

df = pd.read_csv(Input_File)

logging.info("df.index = %s", df.index)
logging.info("df.columns = %s", df.columns)
logging.info("df.describe() = %s", df.describe())

#get a subset of the data frame, still a data frame
dfDateAttributes = df.loc[:,['snapdate']]
logging.info("dfDateAttributes = %s", dfDateAttributes)
print dfDateAttributes.groupby(by='snapdate').size().plot.bar()
plt.axhline(0, color='yellowgreen')
plt.show()





