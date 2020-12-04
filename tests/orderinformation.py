# orderinformation.py #
# Author: Daniel Zulfic #
# Teacher: Mr. Sean Watson #
# Date: December 4th 2020 #
# Copyright: Daniel Zulfic 2020 #
# Completed test suite for Final Project


class OrderInformation:

    def __init__(self):
        self.quantity = None
        self.productName = None
        self.productId = None
        self.allergies = None
        self.comments = None

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def set_productName(self, productName):
        self.productName = productName

    def get_productName(self):
        return self.productName

    def set_productId(self, productId):
        self.productId = productId

    def get_productId(self):
        return self.productId

    def set_allergies(self, allergies):
        self.allergies = allergies

    def get_allergies(self):
        return self.allergies

    def set_comments(self, comments):
        self.comments = comments

    def get_comments(self):
        return self.comments