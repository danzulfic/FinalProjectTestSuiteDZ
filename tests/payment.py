# payment.py #
# Author: Daniel Zulfic #
# Teacher: Mr. Sean Watson #
# Date: December 4th 2020 #
# Copyright: Daniel Zulfic 2020 #
# Completed test suite for Final Project


import random


class Payment:

    def __init__(self):
        self.paymentId = random.randint(1000,2000)
        self.paymentType = None
        self.currency = None
        self.paymentDate = None

    def get_paymentId(self):
        return self.paymentId

    def set_paymentType(self, paymentType):
        self.paymentType = paymentType

    def get_paymentType(self):
        return self.paymentType

    def set_currency(self, currency):
        self.currency = currency

    def get_currency(self):
        return self.currency

    def set_paymentDate(self, paymentDate):
        self.paymentDate = paymentDate

    def get_paymentDate(self):
        return self.paymentDate