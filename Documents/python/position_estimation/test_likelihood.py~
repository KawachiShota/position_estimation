import serial, time, math
#import pyb
import normal_distribution_likelihood

l_cal = normal_distribution_likelihood.Normal_distribution_likelihood()

received_data1 = -74
received_data2 = -73
a_list = [-71,-73,-69,-74,-74,-70,-68,-66,-72,-68,-69,-75]
d_list = [2,2.9,3.2,4,3.5,3]


while True:

    l_list = l_cal.likelihood(received_data1,received_data2,a_list,d_list)
    print "likelihood=",l_list

    time.sleep(1.0)
