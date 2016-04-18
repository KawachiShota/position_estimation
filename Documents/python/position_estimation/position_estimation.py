import math, copy

#Average and Dispersion

l1_file = open('L1.txt','r')
data_file = open('all_data.txt','r')

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

    def parameter_calculation(self):
        for line in data_file:
            all_list = line.strip().split('\t')
            data = []
            for item in all_list:
                data.append(int(item))
            print data
        lis = data[12]
        print lis
        #a = line, b = column, c = Left or Right


    def likelihood(self, xl,xr):
        self.xl = xl
        self.xr = xr

        alist = [ave1, ave2, ave3, ave4, ave5, ave6]
        pre_llist = []

        for ave in alist:
            total = (xl-ave)**2+(xr-ave)**2
            log_l_cal = -2*math.log(disp)-total/2/disp**2
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
