import serial, math, copy
import numpy as np

class Received_data:

    def __init__(self):
        self.r_data1 = 0
        self.r_data2 = 0

    def received_data1(self):

        serA = serial.Serial('/dev/ttyTHS0', 115200)

        lineA = serA.read(8)
        r_data1 = int(lineA[4:7])

        return r_data1
        serA.close()

    def received_data2(self):

        serB = serial.Serial('/dev/ttyTHS1', 115200)

        lineB = serB.read(8)
        r_data2 = int(lineB[4:7])

        return r_data2
        serB.close()

