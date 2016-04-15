import math

"Average and Dispersion"
ave = -65
disp = 50

"average"
ave1 = -80
ave2 = -75
ave3 = -70
ave4 = -65
ave5 = -60
ave6 = -55

class Bayes_update:

    def __init__(self):
        self.value = 0

    def randum_data(self, value):
        self.value = value
        received_data = value
        return received_data

    def likelihood(self, xl,xr):
        self.xl = xl
        self.xr = xr

        list = [ave1, ave2, ave3, ave4, ave5, ave6]
        likelihood = []
        for ave in list:
            pi = math.pi
            s = math.sqrt(2*pi*disp)
            el = math.exp((-1/(2*disp))*pow((xl-ave),2))
            er = math.exp((-1/(2*disp))*pow((xr-ave),2))

            ll = 1/s*el
            lr = 1/s*er
            l_cal = ll*lr
            likelihood.append(l_cal)
        return likelihood
"""
    def posterior_probability(self,major,minor):

    def judgement(self):


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
        return(dataA)"""

