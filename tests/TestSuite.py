# Final Project Test Suite.py #
# Author: Daniel Zulfic #
# Teacher: Mr. Sean Watson #
# Date: December 4th 2020 #
# Copyright: Daniel Zulfic 2020 #
# Completed test suite for Final Project

# Test for user:
from tests.user import User
from tests.customer import Customer
from tests.order import Order
from tests.orderinformation import OrderInformation
from tests.payment import Payment
from tests.tracking import Tracking

#Test as part of requirement for User security to ensure that the safety system is functioning
def test_user_password():
    user = User()
    user.set_password("Daniel")
    assert user.get_password() == "Daniel", "the password should be Daniel"

#Test as part of requirement for User security. Ensures that the UserIds are within the limits of the system
def test_to_check_userId_between_preset_values():
    user = User()
    assert (user.get_userId() >= 0) & (user.get_userId() <= 100), "the user id should be between 0 and 100"

#Test as a part of Customers data security. Ensuring name is stored to user
def test_setting_customer_name():
    customer = Customer()
    customer.set_name("Danny")
    assert customer.get_name() == "Danny", "name should be Danny"

#Test as part of ensuring a Customer can link an email to their account
def test_setting_customer_email():
    customer = Customer()
    customer.set_email("dannyz@gmail.com")
    assert customer.get_email() == "dannyz@gmail.com", "email should return dannyz@gmail.com"

#Test as a part of ensuring a phone number can be added to the Customer
def test_setting_customer_phone_number():
    customers = Customer()
    customers.set_phoneNumber("5195556666")
    assert customers.get_phoneNumber() == "5195556666", "phone number should be 5195556666"

#Test for order data, ensuring the date is correctly passed through the system
def test_setting_order_date():
    orders = Order()
    orders.set_date("12/03/2020")
    assert orders.get_date() == "12/03/2020", "the date should be 12/03/2020"

#Test for order data, ensuring the customer address is correctly passed through the system
def test_setting_order_address():
    order = Order()
    order.set_address("100 McMaster Dr")
    assert order.get_address() == "100 McMaster Dr", "the address should be 100 McMaster Dr"

#Order price calculation, checks to see if the order price is greater than zero to avoid incorrect payment processing
def test_setting_order_calculation_greater_than_zero():
    order = Order()
    order.orderCalculation(8, 22)
    assert order.get_orderTotal() == 30, "the order total should be 30"

#Order price calculation, instead calculate the situation where they system provides a negative value
def test_setting_order_calculation_less_than_zero():
    order = Order()
    order.orderCalculation(8, -22)
    assert order.get_orderTotal() is None, "the order total should return None"

#Order status test, checks to see if status is correctly passed through system
def test_setting_order_status():
    order = Order()
    order.set_status("Cooking")
    assert order.get_status() == "Cooking", "order status should be Cooking"

#Test to ensure that Order Information in terms of quantity of products purchased is working correctly
def test_setting_order_information_for_quantity():
    order_information = OrderInformation()
    order_information.set_quantity("3 items")
    assert order_information.get_quantity() == "3 items", "order should contain 3 items"

#Test to ensure that Order Information in terms of product names of products purchased is working correctly
def test_setting_order_information_for_productName():
    order_information = OrderInformation()
    order_information.set_productName("Steak")
    assert order_information.get_productName() == "Steak", "order should contain steak"

#Test to ensure that Order Information in terms of ProductIds of products purchased is working correctly
def test_setting_order_information_for_productId():
    order_information = OrderInformation()
    order_information.set_productId("4476")
    assert order_information.get_productId() == "4476", "product id should be 4476"

#Test to ensure that Order Information in terms of user allergies of products purchased is working correctly
def test_setting_order_information_for_allergies():
    order_information = OrderInformation()
    order_information.set_allergies("no allergies")
    assert order_information.get_allergies() == "no allergies", "customer should have no allergies"

#Test to ensure that Order Information in terms of additional user comments or requests of products purchased is working correctly
def test_setting_order_information_for_comments():
    order_information = OrderInformation()
    order_information.set_comments("steak medium rare")
    assert order_information.get_comments() == "steak medium rare", "user should be asking for medium rare steak"

#Payment test to ensure a random paymentId between 1000 and 2000 has been successfully created
def test_to_check_paymentId_between_preset_values():
    payment = Payment()
    assert (payment.get_paymentId() >= 1000) & (
                payment.get_paymentId() <= 2000), "the payment id should be between 1000 and 2000"

#Payment test to verify that payment type is correctly verified by system
def test_setting_payment_type():
    payment = Payment()
    payment.set_paymentType("Visa")
    assert payment.get_paymentType() == "Visa", "payment type should be Visa"

#Payment test to verify payment is being completed in correct currency
def test_setting_payment_currency():
    payment = Payment()
    payment.set_currency("CAD")
    assert payment.get_currency() == "CAD", "payment currency should be CAD"

#Payment test to verify payment date is being processed correctly
def test_setting_payment_date():
    payment = Payment()
    payment.set_paymentDate("12/03/2020")
    assert payment.get_paymentDate() == "12/03/2020", "payment date should be 12/03/2020"

#Tracking test to ensure system is creating a unique trackingId between 2001 and 3000
def test_to_check_trackingId_between_preset_values():
    tracking = Tracking()
    assert (tracking.get_trackingId() >= 2001) & (
                tracking.get_trackingId() <= 3000), "the tracking id should be between 2001 and 3000"

#Tracking test to calculate a delivery time based on food prep time and delivery time
def test_to_calculate_delivery_time():
    tracking = Tracking()
    tracking.calculate_deliveryTime(15, 25)
    assert tracking.get_deliveryTime() == 40, "delivery time should be 40 minutes"
