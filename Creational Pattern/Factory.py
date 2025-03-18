from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def vehicleTravel(self):
        pass

class Car(Vehicle):
    def vehicleTravel(self):
        print("Amma Naanu Caaru!(Language Kannada)")

class Bike(Vehicle):
    def vehicleTravel(self):
        print("Amma naanu Bikuu!")

class Plane(Vehicle):
    def vehicleTravel(self):
        print("Naanu Planu!")
    

class VehicleFactory(ABC):
    @abstractmethod 
    def createVehicle(self) -> Vehicle:
        pass

class CarFactory(VehicleFactory):
    def createVehicle(self):
        return Car()

class BikeFactory(VehicleFactory):
    def createVehicle(self):
        return Bike()
class PlaneFacotory(VehicleFactory):
    def createVehicle(self):
        return Plane()
    

if __name__ == "__main__":
    carF = CarFactory()
    bikeF = BikeFactory()
    planeF = PlaneFacotory()

    car = carF.createVehicle()
    bike = bikeF.createVehicle()
    plane = planeF.createVehicle()

    car.vehicleTravel()
    bike.vehicleTravel()
    plane.vehicleTravel()