def calc_discounted_price(price: float, is_member: bool):
    if is_member:
        return price - price * 0.1
    else:
        return price - price * 0.05

res_price =calc_discounted_price(1000, True)
print(res_price)

# can use both integers and floats
