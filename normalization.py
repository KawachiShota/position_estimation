import math, copy
import numpy as np
import random

class Normalization:

    def __init__(self):
        self.nlist = 0

    def value_normalization(self, nlist):
        self.nlist = nlist

        normallist = []

        ilist = copy.copy(nlist)
        ilist.sort()

        numerator = ilist[2]

        for i in range(0,3):
            normal = (self.nlist[i])/numerator
            normallist.append(normal)
        return normallist



