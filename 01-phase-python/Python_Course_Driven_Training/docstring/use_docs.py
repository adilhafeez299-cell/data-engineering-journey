# Docstrings - documentation strings for functions
# Docstrings explain what a function does, its parameters, and return value
# Access with function_name.__doc__ or help(function_name)

def print_number_info(num):
    """
    Returns info regarding num, whether num is even or odd

    :param int num: Number to be evaluated
    :return str: Returns string which tells whether num is even or odd
    """
    # Check if number is divisible by 2 (no remainder means even)
    if (num % 2) == 0:
        return "Num is even"
    else:
        return "Num is odd"

# Call the function with an even number
print(print_number_info(20))  # Output: "Num is even"

# Function with docstring explaining parameters and return type
def integer_multiplier(num1,num2):
    """
    Multiplies two integers and returns the result as a formatted string

    :param int num1: 1st number to be multiplied
    :param int num2: 2nd number to be multiplied
    :return str : returns result of multiplication of the two parameters, in string format
    """
    # Return formatted string with multiplication result
    return f"The result of multiplication is {num1 * num2}"

# Call function and print result
print(integer_multiplier(10,20))  # Output: "The result of multiplication is 200"


