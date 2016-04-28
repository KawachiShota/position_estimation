import math, copy
import numpy as np
import random
import update


class Prior_distribution:

    def __init__(self):
        self.ynewlist = 0
        self.a = 0

    def prior_probability(self, y_list):
        self.y_list = y_list

        ynew_cal = update.Update()

        if self.a == 0:
            xlist = [math.log(0.33),math.log(0.34),math.log(0.33)]
            self.a = 1
        else:
            xlist = ynew_cal.y_update(y_list)

        return xlist

