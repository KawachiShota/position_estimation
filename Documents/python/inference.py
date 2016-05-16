import math, copy
import random

import numpy as np

#import pandas as pd
#from pandas import Series,DataFrame

import matplotlib.pyplot as plt

#import seaborn as sns

from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB

#-----import modules-----
import newdata
import graph

class NaiveBayes:
    __theta = 0
    __sigma = 0

    def __init__(self):
        pass 
        #self.__new_data = 0

    def learning(self,x_data,y_data):
        self.rssi = np.loadtxt(x_data, delimiter=',')
        print(self.rssi)

        self.position = np.loadtxt(y_data, delimiter=',')
        print(self.position)

        self.gaussian_nb = GaussianNB()

        from sklearn.cross_validation import train_test_split
        rssi_train, rssi_test, position_train, position_test = train_test_split(self.rssi, self.position, random_state=0)

        self.gaussian_nb.fit(rssi_train,position_train)
        print("theta",self.gaussian_nb.theta_)
        print("sigma",self.gaussian_nb.sigma_)

        predicted = self.gaussian_nb.predict(rssi_test)

        print(metrics.accuracy_score(position_test, predicted))
    '''
    def set_params(self,theta,sigma):
        __theta = theta
        __sigma = sigma
        print __theta
        print __sigma
        '''

    def inference(self,r_data):
        self.predicted_class = self.gaussian_nb.predict(r_data)

        post_prob = self.gaussian_nb.predict_proba(r_data)
        log_prob = self.gaussian_nb.predict_log_proba(r_data)
        self.post_prob_float16 = post_prob.astype(np.float16)
        #E = 1*self.post_prob_float16[0][0]+2*self.post_prob_float16[0][1]+3*self.post_prob_float16[0][2]
        #var = (1*self.post_prob_float16[0][0]+4*self.post_prob_float16[0][1]+9*self.post_prob_float16[0][2])-E**2
        #print(self.post_prob_float16)
        #print(self.post_prob_float16[0])
        #print(var)
        print(self.predicted_class)
        #print(self.gaussian_nb.class_prior_)
        #print(log_prob)

        return self.predicted_class

    def output(self):
        output = graph.Graph()
        output.bar_graph(self.post_prob_float16[0])


