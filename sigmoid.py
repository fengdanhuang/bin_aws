

import math

def sigmoid(x):
    a = []
    for item in x:
        a.append(1/(1+math.exp(-(item-4))))
    return a

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10., 10., 0.2)
sig = sigmoid(x)
plt.plot(x,sig)
plt.plot([4], [0.5], marker='o', markersize=6, color="red")
plt.plot([4], [0], marker='o', markersize=3, color="red")
plt.plot([-10], [0.5], marker='o', markersize=3, color="red")
plt.axhline(y=0.5, xmin=-10, xmax=4, linewidth=1, linestyle='--', color='red')
plt.axvline(x=4, ymin=0, ymax = 10, linewidth=1, linestyle='--', color='red')
plt.annotate('0.5)', xy=(4.24,0.5), xytext=(30,0), textcoords='offset points')
plt.annotate('(4,', xy=(4.22,0.5))
plt.show()
