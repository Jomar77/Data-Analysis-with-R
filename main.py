import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm


#create a data analysis project on age demographics

#read in the data
data = sp.genfromtxt("web_traffic.tsv", delimiter="\t")

#split the data into x and y
x = data[:,0]
y = data[:,1]

#clean the data
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

#plot the data
plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)], ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()

#fit the data with a polynomial
fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
print ("Model parameters: %s" % fp1)
print (residuals)

f1 = sp.poly1d(fp1)