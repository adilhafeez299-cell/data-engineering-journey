user_dict = {}

key1 = input("Enter the name of the first key:")
value1 = input("Enter the value for this key:")
user_dict[key1] = value1

key2 = input("Enter the name of the second key:")
value2 = input("Enter the value for this key:")
user_dict[key2] = value2

key3 = input("Enter the name of the third key:")
value3 = input("Enter the value for this key:")
user_dict[key3] = value3

#show results
print("\nFinal dictionary:")
print(user_dict)

# go over this again, this relied on input, need 3 name, 3 values, so need to repeat sequence 3 times
# can use loop - wait to learn about loops and how they can be applied to this exercise

#Alternative solution:
user_dict = {}

key1 = input("Key 1: ")
value1 = input("Value 1: ")
user_dict[key1] = value1

key2 = input("Key 2: ")
value2 = input("Value 2: ")
user_dict[key2] = value2

key3 = input("Key 3: ")
value3 = input("Value 3: ")
user_dict[key3] = value3

print(user_dict)