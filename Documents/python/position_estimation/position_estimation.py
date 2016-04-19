import math, copy
import numpy as np

#Average and Dispersion

l1_file = open('L1.txt','r')

ave1 = -80
ave2 = -75
ave3 = -70
ave4 = -65
ave5 = -60
ave6 = -55

disp = 4

class Position_estimator:

    def __init__(self):
        self.value = 0
        self.ylist = 0

    def randum_data(self, value):
        self.value = value
        received_data = value
        return received_data

    def average_calculation(self):
        data = np.loadtxt('all_data.txt',comments='#',delimiter=',')
        print data
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
        print data.shape

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


    def likelihood(self, xl,xr,ave,disp):
        self.xl = xl
        self.xr = xr
        self.ave = ave
        self.disp = disp

        pre_llist = []

        for m in [0,2,4,6,8,10]:
            total = (xl-ave[m])**2+(xr-ave[m+1])**2
            log_l_cal = -2*math.log(disp[m/2])-total/2/(disp[m/2])**2
            l_cal = math.exp(log_l_cal)
            pre_llist.append(l_cal)
        return pre_llist

        #pre_llist.sort()
        #return likelihood

    def posterior_probability(self,xlist,llist):
        self.xlist = xlist
        self.llist = llist

        probability = []

        for i in [0,1,2,3,4,5]:
            x = xlist[i]
            l = llist[i]
            probability_cal = x*l
            probability.append(probability_cal)
        return probability


    def judgement(self,ylist):
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

"""
    def conversion(self):
     
        M = 0
        B = 0
        F = 0
        
        for i in range(0, len(self.slice_list)):
            B += self.slice_list[i][2]
            F += 1

        M = B/F

        dataA = []
        dataA.append(1)
        dataA.append(M)
        return(dataA)

            pi = math.pi
            s = math.sqrt(2*pi*disp)
            el = math.exp((-1/(2*disp))*pow((xl-ave),2))
            er = math.exp((-1/(2*disp))*pow((xr-ave),2))

            ll = 1/s*el
            lr = 1/s*er
            l_cal = ll*lr
            likelihood.append(l_cal)
        return likelihood"""
