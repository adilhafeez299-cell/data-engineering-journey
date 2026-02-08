counter = 0

def inc_counter(value=1):
    """
    Increments value

    :param int value: Increment counter by value, value default to 1
    """
    global counter
    counter += value

def dec_counter(value=1):
    """
        Decrements value

        :param int value: decrements counter by value, value default to 1
        """
    global counter
    counter -= value

inc_counter(20)
print(counter)
dec_counter(17)
print(counter)
dec_counter()
print(counter)
inc_counter(345)
print(counter)