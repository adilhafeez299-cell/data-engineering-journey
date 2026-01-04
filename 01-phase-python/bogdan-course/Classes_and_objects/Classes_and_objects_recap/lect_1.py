class Car:
    def move(self):
        print("Car is moving")
    def stop(self):
        print("Car is stopped")
        # we are creating a class in the above block of code


my_car = Car()
print(type(my_car))
print(isinstance(my_car, Car))


my_car.move()
my_car.stop()
