# Create a base class Vehicle with a meathod move() and two subclasses Car and Bicycle.

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("The car is driving on the road.")

class Bicycle(Vehicle):
    def move(self):
        print("The bicycle is pedaling on the road")


car = Car()
bicycle = Bicycle()
car.move()
bicycle.move()  