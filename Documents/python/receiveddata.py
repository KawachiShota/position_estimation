import serial, math, copy
import numpy as np

class ReceivedData:

    def __init__(self):
        self.r_data1 = 0
        self.r_data2 = 0

    def received_data(self):

        serA = serial.Serial('/dev/ttyTHS0', 115200)
        serB = serial.Serial('/dev/ttyTHS1', 115200)

        lineA = serA.read(19)
        lineB = serB.read(19)

        #r_data1_1 = int(lineA[1:4])
        r_data1_2 = float(lineA[6:11])
        r_data1_3 = float(lineA[13:18])

        #r_data2_1 = int(lineB[1:4])
        r_data2_2 = float(lineB[6:11])
        r_data2_3 = float(lineB[13:18])


        r_data = []
        #r_data.append(r_data1_1)
        #r_data.append(r_data2_1)
        r_data.append(r_data1_2)
        r_data.append(r_data1_3)
        r_data.append(r_data2_2)
        r_data.append(r_data2_3)

        return r_data

        serA.close()
        serB.close()
