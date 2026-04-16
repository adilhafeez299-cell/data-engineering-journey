def nums_info (a,b):
    if (type(a) is not int) or (type(b) is not int):
        return "one of the arguments in not int"
    if a >= b:
        return f"{a} is greater than or equal to {b}"

    return f"{a} is less than {b}"

print(nums_info(True,10))
# One of the arguments is not int
print(nums_info(10,2))
# 10 is greater than or equal to 2
print(nums_info(4,15)) # 4 is less than 15


