import math, copy
import numpy as np
import random

class Normal_distribution_log_likelihood:

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

        for i in range(0,3):
            total = (xl-ave[i*2])**2+(xr-ave[(i*2)+1])**2
            log_l_cal = -2*math.log(math.sqrt(disp[i]))-total/2/(disp[i])
            pre_llist.append(log_l_cal)

        return pre_llist

        """klist = copy.copy(pre_llist)
        klist.sort()
        print klist

        max_l = klist[2]

        llist = []

        for k in range(0,3):
            l_cal = math.exp(pre_llist[k]-max_l)
            print l_cal
            llist.append(l_cal)

        return llist"""

        #pre_llist.sort()
        #return likelihood


