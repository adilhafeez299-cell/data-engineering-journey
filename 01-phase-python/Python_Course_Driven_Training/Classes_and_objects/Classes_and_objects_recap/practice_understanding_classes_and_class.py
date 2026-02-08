class Car:
    def move(self):
        print("Car is moving")
    def stop(self):
        print("Car is stopped")

my_car = Car()
print(type(my_car))
print(isinstance(my_car, Car))
print(isinstance(my_car, object))
print(dir(my_car))


my_car.move()
my_car.stop()

