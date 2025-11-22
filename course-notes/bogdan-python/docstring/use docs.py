def print_number_info(num):
    """
    Returns info regarding num, whether num is even or odd

    :param int num: Number to be evaluated
    :return str: Returns string which tells whether num is even or odd
    """
    if (num % 2) == 0:
        return "Num is even"
    else:
        return "Num is odd"

print(print_number_info(20))

def integer_multiplier(num1,num2):
    """

    :param int num1: 1st number to be multiplied
    :param int num2: 2nd number to be multiplied
    :return str : returns result of multiplication of the two parameters, in string format
    """
    return f"The result of multiplication is {num1 * num2}"


print(integer_multiplier(10,20))


