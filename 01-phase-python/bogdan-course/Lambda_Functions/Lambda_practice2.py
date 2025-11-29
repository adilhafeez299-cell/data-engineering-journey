my_nums = [3, 4, 10, 15, 20, 21]


print(10%2)
print(9%2)
# % modal operator
even_nums = list(filter(lambda num: num % 2 == 0, my_nums))
print(even_nums)

odd_nums = list(filter(lambda num: num % 2 == 1, my_nums))
print(odd_nums)