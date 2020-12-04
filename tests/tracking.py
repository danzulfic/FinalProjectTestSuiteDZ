# tracking.py #
# Author: Daniel Zulfic #
# Teacher: Mr. Sean Watson #
# Date: December 4th 2020 #
# Copyright: Daniel Zulfic 2020 #
# Completed test suite for Final Project


import random


class Tracking:

    def __init__(self):
        self.trackingId = random.randint(2001, 3000)

    def get_trackingId(self):
        return self.trackingId

    def calculate_deliveryTime(self, cookTime, deliveryTime):
        self.estDeliveryTime = cookTime + deliveryTime

    def get_deliveryTime(self):
        if self.estDeliveryTime > 0:
            return self.estDeliveryTime
        else:
            return None
