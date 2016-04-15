import serial, time, math
"import pyb"
import position_estimation

serA = serial.Serial('/dev/ttyTHS0', 115200)
serB = serial.Serial('/dev/ttyTHS1', 115200)

"usb = pyb.USB_VCP()"

p_cal = position_estimation.Bayes_update()

"prior probability"
x1 = 100/6
x2 = 100/6
x3 = 100/6
x4 = 100/6
x5 = 100/6
x6 = 100/6

"iBeacon"
initial_value = -65

while True:

    "r_data = received_data"

    """lineA = serA.read(8)
    received_data_1 = lineA
    lineB = serB.read(8)
    received_data_2 = lineB"""

    r_data_1 = p_cal.randum_data(initial_value)
    r_data_2 = p_cal.randum_data(initial_value)
    print "Data1=",r_data_1
    print "Data2=",r_data_2


    "likelihood = l"
    l = p_cal.likelihood(r_data_1,r_data_2)
    print l

    """
    "posterior_probability = y(1 to 6)"
    y1 = p_cal.posterior_probability(x1,m)
    y2 = p_cal.posterior_probability(x2,m)
    y3 = p_cal.posterior_probability(x3,m)
    y4 = p_cal.posterior_probability(x4,m)
    y5 = p_cal.posterior_probability(x5,m)
    y6 = p_cal.posterior_probability(x6,m)


    "position_judgement"
    position = p_cal.judgement(y1,y2,y3,y4,y5,y6)

    "probability_replacement"
    x1=y1
    x2=y2
    x3=y3
    x4=y4
    x5=y5
    x6=y6

    "send_data"
    send_data = p_cal.conversion(position,r_data_1,r_data_2)
    send_data = []
    send_data.append(position)
    send_date.append(r_data_1)
    send_date.append(r_data_2)
    print send_data
    send_val = str(send_data)
    usb.send(send_val)
    """
    time.sleep(1)

serA.close()
serB.close()
