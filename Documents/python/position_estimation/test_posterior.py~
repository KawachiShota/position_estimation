import serial, time, math
#import pyb
import posterior_distribution

y_cal = posterior_distribution.Posterior_distribution()

x_list = [2,4,6,8,10,12]
l_list = [2,2,2,2,2,2]

while True:

    y_list = y_cal.posterior_probability(x_list,l_list)
    print "posterior_probability=",y_list

    time.sleep(1.0)
