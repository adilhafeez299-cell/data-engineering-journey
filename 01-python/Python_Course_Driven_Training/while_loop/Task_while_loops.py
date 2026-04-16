while True:
  number_1 =  int(input('enter a number'))
  number_2 =  int(input('enter another number'))
  print(number_1/number_2)
  input('Do you want to continue? Yes or no')
  if input == 'no':
      break
  if input == 'yes':
      continue
  print("You must enter two new numbers")

# above is my go at the task

#ammending
while True:
    number_1 = int(input('enter a number: '))
    number_2 = int(input('enter another number: '))
    print(number_1/number_2)

    user_response = input('Do you want to continue? (yes/no): ').lower()
    if user_response == 'no':
        break
    if user_response == 'yes':
        continue
    