# user.py #
# Author: Daniel Zulfic #
# Teacher: Mr. Sean Watson #
# Date: December 4th 2020 #
# Copyright: Daniel Zulfic 2020 #
# Completed test suite for Final Project


import random


class User:

    def __init__(self):
        self.user_Id = random.randint(0, 100)
        self.password = None

    def get_userId(self):
        return self.user_Id
    
    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password
