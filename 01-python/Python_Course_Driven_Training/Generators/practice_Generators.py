
squares_gen = (num * num for num in range(100_000_000))

for num in squares_gen:
    print(num)
    if num == 100:
        break

print("Second Iteration")

for num in squares_gen:
    print(num)
    if num == 225:
        break