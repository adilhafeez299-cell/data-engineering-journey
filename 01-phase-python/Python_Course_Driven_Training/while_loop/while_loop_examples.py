i = 10

while i < 50:
    print(i)
    i += 10


while True:
    print("Infinite loop")
    break


while True:
    answer = input("Enter yes or no:")
    if answer == "no":
        break

import random

random_num = random.randint(1, 10)
while True:
    num = int(input("Enter a number between 1 and 10:"))
    if num != random_num:
        print("Wrong number!")
        continue
    print("Congratulations! you guessed the number!", random_num)
    break

