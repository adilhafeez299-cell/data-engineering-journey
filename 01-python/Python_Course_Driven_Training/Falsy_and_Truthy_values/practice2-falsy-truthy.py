my_dict = {'a':10, 'b': [1,2]}

if len(my_dict) > 0:
    print("Dictionary is not empty")

if len(my_dict):
    print("Dictionary is not empty")

if bool(my_dict):
    print("Dictionary is not empty")

if not my_dict:
    print("Dictionary is empty")
    #if empty returns print statement 

if my_dict.get('b'):
    print("key 'b' in the dictionary value")


