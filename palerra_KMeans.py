#!/Applications/anaconda/bin/python

import sys
import time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans, MiniBatchKMeans

from sklearn.metrics.pairwise import pairwise_distances_argmin


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

dfArray = df.values
print dfArray

dfFeatures = dfArray[:, 6:56]
print dfFeatures

print "dfFeatures.shape = ", dfFeatures.shape

##############################################################################
# Compute clustering with Means
n_clusters = 2

k_means = KMeans(init='k-means++', n_clusters=2, n_init=10)
t0 = time.time()
k_means.fit(dfFeatures)
t_batch = time.time() - t0
k_means_labels = k_means.labels_
k_means_cluster_centers = k_means.cluster_centers_
k_means_labels_unique = np.unique(k_means_labels)

print " k_means_labels = ", k_means_labels
print " k_means_cluster_centers = ", k_means_cluster_centers
print " k_means_labels_unique = ", k_means_labels_unique

##############################################################################
# Compute clustering with MiniBatchKMeans
batch_size = 45
mbk = MiniBatchKMeans(init='k-means++', n_clusters=3, batch_size=batch_size,
                      n_init=10, max_no_improvement=10, verbose=0)
t0 = time.time()
mbk.fit(dfFeatures)
t_mini_batch = time.time() - t0
mbk_means_labels = mbk.labels_
mbk_means_cluster_centers = mbk.cluster_centers_
mbk_means_labels_unique = np.unique(mbk_means_labels)



# Plot result
fig = plt.figure(figsize=(16, 6))
fig.subplots_adjust(left=0.02, right=0.98, bottom=0.05, top=0.9)
colors = ['#4EACC5', '#FF9C34', '#4E9A06']

order = pairwise_distances_argmin(k_means_cluster_centers, mbk_means_cluster_centers)



# KMeans
ax = fig.add_subplot(1, 3, 1)
for k, col in zip(range(n_clusters), colors):
    my_members = k_means_labels == k
    cluster_center = k_means_cluster_centers[k]
    ax.plot(dfFeatures[my_members, 0], dfFeatures[my_members, 1], 'w', markerfacecolor=col, marker='.')
    ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=6)
ax.set_title('KMeans')
ax.set_xticks(())
ax.set_yticks(())
plt.text(-3.5, 1.8,  'train time: %.2fs\ninertia: %f' % (t_batch, k_means.inertia_))

# MiniBatchKMeans
ax = fig.add_subplot(1, 3, 2)
for k, col in zip(range(n_clusters), colors):
    my_members = mbk_means_labels == order[k]
    cluster_center = mbk_means_cluster_centers[order[k]]
    ax.plot(dfFeatures[my_members, 0], dfFeatures[my_members, 1], 'w', markerfacecolor=col, marker='.')
    ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,markeredgecolor='k', markersize=6)
ax.set_title('MiniBatchKMeans')
ax.set_xticks(())
ax.set_yticks(())
plt.text(-3.5, 1.8, 'train time: %.2fs\ninertia: %f' % (t_mini_batch, mbk.inertia_))



plt.show()
