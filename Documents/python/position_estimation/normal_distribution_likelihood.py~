import math, copy
import numpy as np
import random

class Normal_distribution_likelihood:

    def __init__(self):
        self.xl = 0
        self.xr = 0
        self.ave = 0
        self.disp = 0

    def likelihood(self, xl,xr,ave,disp):
        self.xl = xl
        self.xr = xr
        self.ave = ave
        self.disp = disp

        pre_llist = []

        for i in range(0,6):
            total = (xl-ave[i*2])**2+(xr-ave[(i*2)+1])**2
            log_l_cal = -2*math.log(disp[i])-total/2/(disp[i])**2
            l_cal = math.exp(log_l_cal)
            pre_llist.append(l_cal)
        return pre_llist

        #pre_llist.sort()
        #return likelihood


