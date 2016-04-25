import serial, time, math
#import pyb
import position_inference

po_cal = position_inference.Position_inference()

y_list = [0,1,5,3,4,2]

while True:

    position = po_cal.y_judgement(y_list)
    print position

    time.sleep(1.0)
