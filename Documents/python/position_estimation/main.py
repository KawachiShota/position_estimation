import serial, time, math
#import pyb
import position_estimation

serA = serial.Serial('/dev/ttyTHS0', 115200)
serB = serial.Serial('/dev/ttyTHS1', 115200)

#serC = serial.Serial('/dev/ttyACM0')

l_cal = normal_distribution_likelihood.Normal_distribution_likelihood()

#prior_probability
x1 = 100/6
x2 = 100/6
x3 = 100/6
x4 = 100/6
x5 = 100/6
x6 = 100/6

x = [x1, x2, x3, x4, x5, x6]

#iBeacon
initial_value1 = -79
initial_value2 = -71

#value for check
p_check = 1
column1 = (p_check-1)*2
column2 = (p_check-1)*2 + 1

line1 = 0
line2 = 0

#parameter_calculation(Average and Dispersion)
average = p_cal.average_calculation()
dispersion = p_cal.dispersion_calculation(average)

while True:

    #r_data = received_data
    #lineA = serA.read(8)
    #r_data_1 = int(lineA[4:7])

    #lineB = serB.read(8)
    #r_data_2 = int(lineB[4:7])

    r_data_1 = l_cal.likelihood_data1(line1,column1)
    r_data_2 = p_cal.random_data2(line2,column2)
    print "Data1=",r_data_1
    print "Data2=",r_data_2


    #likelihood
    likelihood = p_cal.likelihood(r_data_1,r_data_2,average,dispersion)
    print "likelihood=",likelihood


    #posterior_probability = y(1 to 6)
    y = p_cal.posterior_probability(x,likelihood)
    print "posterior_probability=",y

    #position_judgement
    position = p_cal.judgement(y)
    print "position=",position


    #probability_replacement
    x = y
    print "x=",x

    #send_data
    #ser.write(str(position))

    time.sleep(1.0)

serA.close()
serB.close()
