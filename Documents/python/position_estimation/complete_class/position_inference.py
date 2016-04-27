import serial, math, copy
import numpy as np
import random

class Position_inference:

    def __init__(self):
        self.value = 0
        self.ylist = 0

    def y_judgement(self,ylist):
        self.ylist = ylist
        serC = serial.Serial("/dev/ttyACM0")

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
            po = 1

        elif j == p2:
            po = 2

        elif j == p3:
            po = 3

        elif j == p4:
            po = 4

        elif j == p5:
            po = 5

        elif j == p6:
            po = 6

        serC.write(str(po))
        return po


