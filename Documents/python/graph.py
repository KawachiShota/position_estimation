import numpy as np

#import pandas as pd
#from pandas import Series,DataFrame

import matplotlib.pyplot as plt

#import seaborn as sns

from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB

class Graph:

    def bar_graph(self,y):
        x=[1,2,3,4]
        plt.bar(x,y)
        plt.show()
