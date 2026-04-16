def check_shipping_fee(weight):
    if weight <= 0:
        print("Invalid weight. Weight must be greater than zero ")

    elif 0 < weight <= 5:
        print("The shipping fee is 5$")

    elif 5 < weight <= 15:
        print("The shipping fee is 10$")

    else:
        print("The shipping fee is 20$")

check_shipping_fee(11.5)
