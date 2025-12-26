from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

all_nums = [-3,1,0,10,-20,5]
absolute_nums = []
for num in all_nums:
    absolute_nums.append(abs(num))

print(absolute_nums)


all_nums = [-3,1,0,10,-20,5]
absolute_nums = [abs(num) for num in all_nums]
print(absolute_nums)
print(all_nums)


all_nums = [-3,1,0,10,-20,5]
positive_nums = []

for num in all_nums:
    if num > 0:
        positive_nums.append(num)
print(positive_nums)

all_nums = [-3,1,0,10,-20,5]
positive_nums = [num for num in all_nums if num > 0]
print(positive_nums)
print(all_nums)



my_set = {10, 20, 223, 45, 20}
new_set = set()

for val in my_set:
    new_set.add(val*val)

print(my_set)
print(new_set)


my_set = {10,20, 223, 43}
new_set = {val*val for val in my_set}
print(new_set)


my_score = {
    'a': 10,
    'b': 7,
    'm': 14
}
scores = {}
for key, value in my_score.items():
    scores[key] = value* 10
print(scores)
print(my_score)

#example 4
my_scores = {
    'a':10,
    'b':7,
    'm':14
}
scores = {k: v*10 for k, v in my_scores.items()}
print(scores)
print(my_scores)
