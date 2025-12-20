
def check_shipping_fee(weight):

    if weight <= 0:
        print("Invalid weight. Weight must be greater than zero ")

    if 0 < weight <= 5:
        print("The shipping fee is 5$")

    if 5 < weight <= 15:
        print("The shipping fee is 10$")

    if weight > 15:
        print("The shipping fee is 20$")

# Additionally, if the weight value is a float, print a note about rounding
    if isinstance(weight, float):
        print("Weight will be rounded up to the nearest integer")

check_shipping_fee(11.5)