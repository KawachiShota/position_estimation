import serial, time, math
import received_data

r_cal = received_data.Received_data()

while True:

    r_data_1 = r_cal.received_data1()
    r_data_2 = r_cal.received_data2()
    print "Data1=",r_data_1
    print "Data2=",r_data_2

    time.sleep(1.0)


