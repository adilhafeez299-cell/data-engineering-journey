#Abstraction
from abc import ABC, abstractmethod

class Payment(ABC):
    def process_payment(self):
        pass

class CreditCardPayment(Payment):
    def process_payment(self):
        pass

class StripePayment(Payment):
    def process_payment(self):
        pass

class PaypalPayment(Payment):
    def process_payment(self):
        pass
