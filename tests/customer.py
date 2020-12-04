class Customer:

    def __init__(self):
        self.name = None
        self.emailAddress = None
        self.phoneNumber = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_email(self, emailAddress):
        self.emailAddress = emailAddress

    def get_email(self):
        return self.emailAddress

    def set_phoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def get_phoneNumber(self):
        return self.phoneNumber


