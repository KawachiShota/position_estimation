import serial, math, copy
import numpy as np
import random

class SendData:

    def __init__(self):
        self.p = 0

    def transmission(self,data):
        self.data = data

        p = str(data[0])
        print p
        serC = serial.Serial("/dev/ttyACM0")
        serC.write(str(p))
        serC.close()

