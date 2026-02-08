class Car :
    def move(self):
        print("Car is moving")
    def stop(self):
        print("Car is stopped")

my_car = Car()
print(type(my_car))
print(isinstance(my_car, Car))
print(isinstance(my_car, object))
print(dir(my_car))
print(my_car.__dict__)


my_car.move()
my_car.stop()

#Speeding example
class car:
    def __init__(self, speed = 0):
        self.speed = speed # car Has a speed
    def move(self):
        print("car is moving")
    def stop(self):
        print("car is stopped")
    def speeding(self):
        if self.speed >= 60:
            print(f"speeding, you too fast, you need to slow down, your speed is {self.speed}")
            print("stopping car")
        else:
            print("you are fine")


my_car = car(100)
my_car.move()
my_car.speeding()
my_car.stop()
