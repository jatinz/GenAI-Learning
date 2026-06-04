from abc import ABC,abstractmethod

class Vehicle:
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car Engine Start"
    
car = Car
print(f" :: {car.start(None)}")