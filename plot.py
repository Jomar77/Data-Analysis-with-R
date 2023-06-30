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
fx = sp.linspace(0, x[-1], 1000)
plt.plot(fx, f1(fx), linewidth=4)
plt.legend(["d=%i" % f1.order], loc="upper left")
plt.show()

#fit the data with a polynomial
fp2, residuals, rank, sv, rcond = sp.polyfit(x, y, 2, full=True)
print ("Model parameters: %s" % fp2)
print (residuals)

f2 = sp.poly1d(fp2)

plt.plot(fx, f2(fx), linewidth=4)
plt.legend(["d=%i" % f2.order], loc="upper left")
plt.show()

#fit the data with a polynomial
fp3, residuals, rank, sv, rcond = sp.polyfit(x, y, 3, full=True)
print ("Model parameters: %s" % fp3)
print (residuals)
