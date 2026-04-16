# Define variables of different data types
age = 26                              # Integer
height = 5.9                          # Float
name = "Adil"                         # String
is_learning_python = True             # Boolean
goals = ['Health', 'Career', 'Family'] # List

# Print each variable along with its data type
print(age, type(age))                 # <class 'int'>
print(height, type(height))           # <class 'float'>
print(name, type(name))               # <class 'str'>
print(is_learning_python, type(is_learning_python)) # <class 'bool'>
print(goals, type(goals))             # <class 'list'>

# Modify variables using different methods
age+= 1                               # Increment age by 1 (now 27)
name.upper()                          # Convert name to uppercase (returns new string, doesn't modify original)
goals.append("Discipline")            # Add "Discipline" to the goals list (modifies list in place)

# Print updated variables
print("\nUpdated:")
print(age, type(age))                 # 27, still int
print(name, type(name))               # "Adil" (unchanged because .upper() doesn't modify in place)
print(goals, type(goals))             # List now has 4 elements