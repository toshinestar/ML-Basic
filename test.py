import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.special import comb
from scipy import mean
from itertools import combinations
from scipy.spatial.distance import cosine
from scipy.spatial.distance import squareform
from scipy.stats import pearsonr

def scatterPlot (data,membership,centroids=None,plotTitle = "The Dataset"):
    """
    This function draw a scatter plot of data points with cluster membership given.
    
    :param data: a numpy array of data points. 
    :param membership: a list of cluster membership of each of the data points in `data'.
                       a membership value can be any natural number beginning with 1, 2, ...
    :param centroids: a numpy array of centroids (optional)
    
    param plotTitle: The title of the plot. Defaults to "The Dataset"
    
    return nothing. But it draws a scatter plot of the data points and centroids are marked with asterisks.
    """
    data = np.array(data)
    membership = np.array(membership)
    
    n,m = data.shape
    assert m==2 #maximum 2-dim samples due to the fact that it's a scatter plot
    k = len(centroids)
    assert(k<=7) #Maximum 7 clusters due to limitation of available colors
    plt.figure(num=None, figsize=(6, 6), dpi=80)
    colorArray = []
    available_colors = ["","b","g","r","c","m","y","k"]
    for i in membership:
        colorArray.append(available_colors[i])
        
    plt.scatter(data[:,0],data[:,1],facecolor="none", edgecolors=colorArray, s=30)
    if centroids is not None:
        for i in range(len(centroids)):
            plt.scatter(centroids[i,0],centroids[i,1],
                        facecolor="none",edgecolors=available_colors[i+1],marker="*",s=150)
    plt.title(plotTitle)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()