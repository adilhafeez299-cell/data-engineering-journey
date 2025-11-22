# Define a global variable 'c' accessible from anywhere in the module
c = True # inside global scope

# Define a function that multiplies two numbers
def mult(a, b):
    # a and b are local variables (function parameters)
    # This function uses only local scope - no global variables accessed
    return a * b


