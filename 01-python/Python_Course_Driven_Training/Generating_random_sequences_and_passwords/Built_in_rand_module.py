import random

print(random.random())
# print(dir(random))
print(random.uniform(10.5,11.6))

#int
print(random.randint(100,1000))
print(random.randint(100,100))

#shuffle
my_list = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(my_list)
print(my_list)

print(random.choice('Adil'))
print(random.choice((1,3,10)))
print(random.choice((1,2,3,4,5,6,7,8,9,10)))
print(random.choice(['a', True, None]))

#Choices
print(random.choices([1,2,3,4,5,], k=5))
print(random.choices('abcdef', k=10))

#create password (not recommended)
print(''.join(random.choices('ABCDEF0123456789', k=12)))

#sample
print(random.sample([1,2,3,4,5], k=5))
print(random.sample([1,1,1,1], k=3))
