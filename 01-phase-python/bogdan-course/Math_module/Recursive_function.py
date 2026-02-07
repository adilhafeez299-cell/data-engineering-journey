import math

def calc_factorial(num: int):
    if type(num) is not int:
        raise TypeError('num must be an integer')
    if num == 0:
        raise ValueError("Num must be positive")
    if num == 1:
        return 1
    return num* calc_factorial(num - 1)

print(calc_factorial(10))
print(math.factorial(10))