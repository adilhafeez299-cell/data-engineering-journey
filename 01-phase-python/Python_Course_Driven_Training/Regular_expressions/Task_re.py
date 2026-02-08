#Password verification task
#Create a function to verify password
#The password must be at least 8 characters long

#Password must contain:
#Lowercase letters
#Uppercase letters
#Numbers
#Special Symbols





#recommendation, create loop as user to create password multiple times

import re

def verify(password):
    if len(password) < 8:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    return True

while True:
    password = input("Create a password:")

    if verify(password):
        print(f"password has been created successfully, your password is: {password}")
        break
    else:
        print("Invalid password. Please try again.")

