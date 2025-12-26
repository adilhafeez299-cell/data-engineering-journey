while True:
    print("we are in the loop")
    # such condition is always truthy don't print infinite loop
    # instead break the loop
    break

username = ''

while not username:
    entered_username = input("Enter your username:")
    if len(entered_username) >= 5:
        username = entered_username
    else:
        print("Username must be at least 5 characters long!")
print("Welcome", username)


import time

seconds_qty = 5

while seconds_qty > 0:
  print(f"Timer: {seconds_qty} seconds remaining")
  seconds_qty -= 1
  time.sleep(1)

print("Time's up!")
