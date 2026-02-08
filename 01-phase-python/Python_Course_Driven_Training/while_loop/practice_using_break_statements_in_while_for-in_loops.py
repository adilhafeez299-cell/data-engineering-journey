user_password = "Admin123"
password = ''

while password != user_password:
    print("Enter 'quit' in order to exit the program")
    password = input("please enter your password:")
    if password == 'quit':
        print("Goodbye!")
        break

if password == user_password:
    print("Login successful!")
else:
    print("Login failed!")



my_list = [10, 4, 3, 4, 2002, 20, 2]

for num in my_list:
    if num == 2:
        break
    print(num)