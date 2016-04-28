import serial, math, copy
import numpy as np
import random

class Position_inference:

    def __init__(self):
        self.value = 0
        self.ylist = 0

    def y_judgement(self,ylist):
        self.ylist = ylist
        #serC = serial.Serial("/dev/ttyACM0")

        p1 = ylist[0]
        p2 = ylist[1]
        p3 = ylist[2]      

        jlist = copy.copy(ylist)
        jlist.sort()
        j = jlist[2]

        print "jlist=",jlist
        print "ylist=",ylist

        if j == p1:
            po = 1

        elif j == p2:
            po = 2

        elif j == p3:
            po = 3

        #serC.write(str(po))
        return po


