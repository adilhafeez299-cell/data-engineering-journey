set1 = {1, 2, 3, 4, 5}
set1.add(6)

set2 = {4,5,6,7,8}

common = set1.intersection(set2)
common_list = list(common)
print(common_list)
print(type(common_list))