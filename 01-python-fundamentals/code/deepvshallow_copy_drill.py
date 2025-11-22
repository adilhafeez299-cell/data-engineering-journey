# Example 1: Assignment (not a copy) - both variables reference the same object
#a = [1, 2, 3]
#b = a  # b points to the same list object as a
#b.append(4)
#print(a)  # [1, 2, 3, 4] - a is also modified!
#print(b)  # [1, 2, 3, 4]
# Both will be appended even if we just want to append b as they point to the same object
#print(id(a),id(b))  # Same memory addresses

# Example 2: Shallow copy - creates new outer list but nested lists are still references
a = [[1,2],[3,4]]
b = a.copy()  # Shallow copy: new list, but inner lists are still shared
b[0].append(99)  # Modifying inner list affects both a and b
print(id(a),id(b))        # Different outer list IDs
print(id(a[0]), id(b[0])) # Same inner list IDs (still references!)
print(id(a[1]), id(b[1])) # Same inner list IDs
print(a)  # [[1, 2, 99], [3, 4]] - a is modified because inner lists are shared!
print(b)  # [[1, 2, 99], [3, 4]]

# Example 3: Deep copy - creates completely independent copies
from copy import deepcopy
a = [[1, 2], [3, 4]]
a = deepcopy(a)  # Deep copy of a (but this line reassigns a, which is confusing)
b[0].append(99)  # Modifying b (which still points to the shallow copy from above)
print(id(a),id(b))  # Different IDs
print(a)  # [[1, 2], [3, 4]] - a is unaffected because it's a deep copy
print(b)  # [[1, 2, 99, 99], [3, 4]] - b has the modification