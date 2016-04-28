import math, copy
import numpy as np
import random

class Posterior_distribution:

    def __init__(self):
        self.xlist = 0
        self.llist = 0

    def posterior_probability(self,xlist,llist):
        self.xlist = xlist
        self.llist = llist

        ylist = []

        for i in range(0,3):
            x = xlist[i]
            l = llist[i]
            probability_cal = x+l
            ylist.append(probability_cal)
        return ylist

