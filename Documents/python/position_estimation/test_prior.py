import serial, time, math
#import pyb
import prior_distribution

x_cal = prior_distribution.Prior_distribution()

y_new = [0,1,2,3,4,5]

while True:

    x_list = x_cal.prior_probability()
    print x_list

    time.sleep(1.0)
