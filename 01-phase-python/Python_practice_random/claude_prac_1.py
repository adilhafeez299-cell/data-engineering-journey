def check_odd_even(num):
    # This only does the math
    num = int(num)
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def check_this(num):
    #this only handle confirmation
    confirm = input(f"you entered {num}. Do you want to continue? (y/n) ").strip().lower()
    return confirm in ["y", "yes"]

#--- Execution Flow ---


# 2. Ask for confirmation second
while True:
  user_input = input("\nEnter a number (or 'quit' to exit: )").strip().lower()

  if user_input == "quit":
      print("Goodbye!")
      break

  if check_this(user_input):
      #3. perform the math and show the result
    result = check_odd_even(user_input)
    print(f"{user_input} is {result}")

  else:
      print("Action Cancelled. Maybe try again when you are a bit more decisive")
