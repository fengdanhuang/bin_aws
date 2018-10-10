#!/Applications/anaconda/bin/python
#owner: Chao Feng, chao.f.feng@oracle.com

#import python lib:
import sys
import os
import logging
import math
import hashlib

#import scipy lib:
import pandas as pd
import numpy as np
from scipy import stats
from scipy.spatial import distance

#import sklearn lib:
from sklearn import preprocessing
from sklearn import cluster
from sklearn.cluster import KMeans
#pd.options.mode.chained_assignment = None

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)


def ZScore_Coor(dfTrain, clusterObj, NOfCluster, dfTest, predictLabels):

	Label = pd.DataFrame(clusterObj.labels_, index=np.arange(len(clusterObj.labels_)), columns=['label'])
	dfTrainL = pd.concat([dfTrain, Label],axis=1)
	
	meanDF = pd.DataFrame()
	stdDF = pd.DataFrame()
	for i in np.arange(NOfCluster):
		dfTrainLi = dfTrainL[dfTrainL.label == i]
		meanS = dfTrainLi.mean()
		stdS = dfTrainLi.std()
		meanDF = meanDF.append(meanS, ignore_index=True)
		stdDF = stdDF.append(stdS, ignore_index=True)
	meanDF.drop(['label'], axis=1, inplace=True)
	stdDF.drop(['label'], axis=1, inplace=True)

	meanL = meanDF.values.tolist()
	stdL = stdDF.values.tolist()

	#Extend the mean and std
	meanExpL = []
	stdExpL = []
	for i in np.arange(len(dfTest.index)):
		meanExpL.append(meanL[predictLabels[i]])
		stdExpL.append(stdL[predictLabels[i]])
	meanExpDF = pd.DataFrame(np.asarray(meanExpL), columns=dfTest.columns)
	stdExpDF = pd.DataFrame(np.asarray(stdExpL), columns=dfTest.columns)

	#Calculte z score based on coordination
	Zero = np.zeros((len(dfTest.index),len(dfTest.columns)))
	ZL = []
	for i in np.arange(len(dfTest.index)):
		nume = distance.euclidean(dfTest.loc[i], meanExpDF.loc[i])
		denom = distance.euclidean(stdExpDF.loc[i], Zero[i]) / math.sqrt(dfTest.shape[1])
		if denom == 0:
			z = np.nan
		else:
			z = nume / denom
		ZL.append(z)
	ZScore = np.asarray(ZL)
	return ZScore






###---Process Argument
paraLimit = 6
if len(sys.argv) < paraLimit:
	logging.info("\n	Usage: ProgramName NOfCluster Train_Preprocess(1/0) Test_Preprocess(1/0) train_file(.csv) test_file(.csv)\n")
	sys.exit(0)

NOfPara = len(sys.argv)
program = sys.argv[0]
NOfCluster = int(sys.argv[1])
ppTrainBool = int(sys.argv[2])
ppTestBool = int(sys.argv[3])
train_file = sys.argv[4]
test_file = sys.argv[5]

logging.info("\nThe number of arguments are: %s\n", NOfPara)
logging.info("The program is: %s", program)
logging.info("The number of clusters is: %s", NOfCluster)

if ppTrainBool == 0:
	logging.info("No preprocessing for train set.")
elif ppTrainBool == 1:
	logging.info("Do preprocessing for test set.")
else:
	logging.info("Preprocessing code for train set invalid!")
	sys.exit(0)

if ppTestBool == 0:
	logging.info("No preprocessing for train set.")
elif ppTestBool == 1:
	logging.info("Do Preprocessing for test set.")
else:
	logging.info("Preprocessing code for test set invalid!")
	sys.exit(0)

logging.info("The input training set is: %s", train_file)
logging.info("The input test set is: %s\n", test_file)


###---Data Process
dfTrain = pd.read_csv(train_file)
dfTest  = pd.read_csv(test_file)
#print "dfTrain = \n", dfTrain
#print "dfTest = \n", dfTest

print "dfTrain.shape = ", dfTrain.shape
print "dfTest.shape = ", dfTest.shape


dfTrain1 = dfTrain.drop(['evntactor'], axis=1)
dfTest1 = dfTest.drop(['evntactor'], axis=1)

features_dfTrain1 = set(dfTrain1.columns.tolist())
features_dfTest1 = set(dfTest1.columns.tolist())
featuresCommon = list(features_dfTrain1.intersection(features_dfTest1))#get the common features of train and test
print "featuresCommon = ", featuresCommon

dfTrain2 = dfTrain1.loc[:,featuresCommon]
dfTest2 = dfTest1.loc[:,featuresCommon]

if ppTrainBool == 0:
	dfTrain3 = dfTrain2
elif ppTrainBool == 1:
	ppObj = preprocessing.MinMaxScaler(feature_range=(0, 100),copy=True)
	dfTrain2PPA = ppObj.fit_transform(dfTrain2)
	dfTrain2PP = pd.DataFrame(dfTrain2PPA, columns = dfTrain2.columns)
	dfTrain3 = dfTrain2PP

if ppTestBool == 0:
	dfTest3 = dfTest2
elif ppTestBool == 1:
	ppObj = preprocessing.MinMaxScaler(feature_range=(0, 100),copy=True)
	dfTest2PPA = ppObj.fit_transform(dfTest2)
	dfTest2PP = pd.DataFrame(dfTest2PPA, columns = dfTest2.columns)
	dfTest3 = dfTest2PP
	

clusterObj = cluster.KMeans(    n_clusters = NOfCluster,
				init = 'k-means++',
				n_init = 15,
				max_iter = 400,
				tol = 0.0001,
				precompute_distances = True,
				verbose = 0,
				random_state = None,
				copy_x = True,
				n_jobs = 1)

clusterObj.fit(dfTrain3)
print "trainLabels = ", clusterObj.labels_
print "trainInertia = ", clusterObj.inertia_
predictLabels = clusterObj.predict(dfTest3)
print "predictLabels = ", predictLabels


zscore = ZScore_Coor(dfTrain3, clusterObj, NOfCluster, dfTest3, predictLabels)
print "zscore = ", zscore


dfkey = pd.DataFrame([{'Tenantid':'384c0e44-ca84-4f92-bb32-24bbe49413b1'}])
dfKey = pd.concat([dfkey]*dfTest.shape[0], ignore_index=True)
dfKey['evntactor'] = dfTest.loc[:,['evntactor']]
dfKey['Userid'] = dfKey['evntactor'].apply(hash)
dfKey['Userid'] = dfKey['evntactor'].apply(lambda row:hashlib.sha256(str(row)).hexdigest())
dfKey['z_score'] = zscore
dfp = pd.DataFrame([{'Algorithm name':'KMean',
		     'Anomaly class':'PEER_GROUP_ANOMALY',
	             'Description':'The user behaved differently from his or her group member'}])
df_P = pd.concat([dfp]*dfTest.shape[0], ignore_index=True)
dfTestFinal = pd.concat([dfKey, df_P], axis=1)
dfTestFinal = dfTestFinal[(dfTestFinal.z_score >= 5.0) & (dfTestFinal.z_score <= 10.0)]
dfTestFinal['Score'] = np.round_(1 / (1 + np.exp((-1)*dfTestFinal['z_score'])),decimals=4)
print "dfTestFinal = \n", dfTestFinal
dfTrition = dfTestFinal.drop(['evntactor','z_score'], axis=1)
print "dfTrition = \n", dfTrition

Output_Trition = "20170908_Anomaly_KMeans_Trition.txt"
logging.info("The Output Trition File Name is:%s\n", Output_Trition)
dfTrition.to_csv(Output_Trition, sep=',',encoding='utf8',index=False)
