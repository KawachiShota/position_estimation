import serial, time, math
#import pyb
import normal_distribution_parameter

pa_cal = normal_distribution_parameter.Normal_distribution_parameter()

while True:

    a_list = pa_cal.average_calculation()
    d_list = pa_cal.dispersion_calculation(a_list)

    time.sleep(1.0)
