import math, copy
import numpy as np
import random

class Normal_distribution_parameter:

    def __init__(self):
        self.value = 0
        self.ylist = 0


    def average_calculation(self):
        data = np.loadtxt('all_data.txt',comments='#',delimiter=',')
        #print data
        print data.shape

        alist = []

        for j in range(0,data.shape[1]):
            pre_alist = []
            for i in range(0,data.shape[0]):
                pre_alist.append(data[i,j])
            pre_ave = sum(pre_alist)/len(pre_alist)
            alist.append(pre_ave)
        print alist
        return alist

    def dispersion_calculation(self,ave_cal):
        self.ave_cal = ave_cal
        data = np.loadtxt('all_data.txt',comments='#',delimiter=',')
        #print data.shape

        dlist = []

        for j in range(0,(data.shape[1]/2)):
            pre_dlist = []
            for i in range(0,data.shape[0]):
                d_cal = pow((data[i,j*2]-ave_cal[j*2]),2) + pow((data[i,j*2+1]-ave_cal[j*2+1]),2)
                pre_dlist.append(d_cal)
            pre_disp = sum(pre_dlist)/len(pre_dlist)/2
            dlist.append(pre_disp)
        print dlist
        return dlist



