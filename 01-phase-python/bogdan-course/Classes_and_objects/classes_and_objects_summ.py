class car:
    def move(self):
        print("Moving car")
    def stop(self):
        print("Stopping car")

my_car = car()
my_car.move()
my_car.stop()

print(type(my_car))
print(isinstance(my_car, car))
