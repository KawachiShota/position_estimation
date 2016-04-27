import math, copy
import numpy as np
import random
import update


class Prior_distribution:

    def __init__(self):
        self.ynewlist = 0
        self.a = 0

    def prior_probability(self):

        ynew_cal = update.Update()

        y_list = [0,1,2,3,4,5]

        if self.a == 0:
            xlist = [100/6,100/6,100/6,100/6,100/6,100/6]
            self.a = 1
        else:
            xlist = ynew_cal.y_update(y_list)

        return xlist

