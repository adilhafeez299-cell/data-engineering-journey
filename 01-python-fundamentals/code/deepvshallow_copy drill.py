#a = [1, 2, 3]
#b = a
#b.append(4)
#print(a)
#print(b)
# both will be appended even if we just want to append be as they point to the same object
#print(id(a),id(b))

a = [[1,2],[3,4]]
b = a.copy()
b[0].append(99)
print(id(a),id(b))
print(id(a[0]), id(b[0]))
print(id(a[1]), id(b[1]))
print(a)
print(b)

from copy import deepcopy
a = [[1, 2], [3, 4]]
a = deepcopy(a)
b[0].append(99)
print(id(a),id(b))
print(a)
print(b)