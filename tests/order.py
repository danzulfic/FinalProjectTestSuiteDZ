# order.py #
# Author: Daniel Zulfic #
# Teacher: Mr. Sean Watson #
# Date: December 4th 2020 #
# Copyright: Daniel Zulfic 2020 #
# Completed test suite for Final Project


class Order:

    def __init__(self):
        self.dateCreated = None
        self.customerAddress = None
        self.orderPrice = None
        self.status = None
        self.total = None

    def set_date(self, dateCreated):
        self.dateCreated = dateCreated

    def get_date(self):
        return self.dateCreated

    def set_address(self, customerAddress):
        self.customerAddress = customerAddress

    def get_address(self):
        return self.customerAddress

    def orderCalculation(self, foodPrice, deliveryPrice) -> int:
        self.total = foodPrice + deliveryPrice
        
    def get_orderTotal(self) -> int:
        if self.total >= 0:
            return self.total
        else:
            return None
    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status