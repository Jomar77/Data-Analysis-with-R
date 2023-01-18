import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm


#create a data analysis project on age demographics

#read in the data
data = sp.genfromtxt("web_traffic.tsv", delimiter="\t")
