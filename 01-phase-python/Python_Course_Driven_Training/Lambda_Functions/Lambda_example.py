def greeting(greet):
    return lambda name: f"{greet}, {name}"
morning_greeting = greeting("Good morning")
print(morning_greeting("Bogdan"))
evening_greeting = greeting("Good evening")
print(evening_greeting("Bogdan"))

def multiply_by(multiplier):
    return lambda x: x *multiplier

multiply_by_3 = multiply_by(3)
print(multiply_by_3(10))
print(multiply_by_3(50))


multiply_by_5 = multiply_by(5)
print(multiply_by_5(10))
print(multiply_by_5(50))