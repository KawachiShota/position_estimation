import serial, time, math

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

import receiveddata
import inference
import senddata

#instance
r_cal = receiveddata.ReceivedData()
nb = inference.NaiveBayes()
send = senddata.SendData()

while True:

    r_data = r_cal.received_data()
    print "Data=",r_data

    nb.learning('data_rssi_ultrasonic_0513.txt','data_position_0511.txt')
    #nb.get_newdata()
    position = nb.inference(r_data)
    #nb.output()

    send.transmission(position)

    time.sleep(0.5)

