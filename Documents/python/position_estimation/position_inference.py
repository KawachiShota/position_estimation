import math, copy
import numpy as np
import random

class Position_inference:

    def __init__(self):
        self.value = 0
        self.ylist = 0

    def y_judgement(self,ylist):
           self.ylist = ylist

           p1 = ylist[0]
           p2 = ylist[1]
           p3 = ylist[2]
           p4 = ylist[3]
           p5 = ylist[4]
           p6 = ylist[5]          


           jlist = copy.copy(ylist)
           jlist.sort()
           j = jlist[5]

           print "jlist=",jlist
           print "ylist=",ylist

           if j == p1:
               return 1
           elif j == p2:
               return 2
           elif j == p3:
               return 3
           elif j == p4:
               return 4
           elif j == p5:
               return 5
           elif j == p6:
               return 6

