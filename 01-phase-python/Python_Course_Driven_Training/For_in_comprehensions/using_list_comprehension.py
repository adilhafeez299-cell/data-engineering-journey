nums = [10, 2, 5, 100]
squared_nums = []

for num in nums:
    squared_nums.append(num*num)
print(squared_nums)
print(nums)

# no using list comprehension
squared_nums = [num*num for num in nums]
print(squared_nums)