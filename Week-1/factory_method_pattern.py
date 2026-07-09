from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):
        return "Driving a Car"


class Bike(Vehicle):
    def drive(self):
        return "Riding a Bike"


class Truck(Vehicle):
    def drive(self):
        return "Driving a Truck"


class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type.lower() == "car":
            return Car()
        elif vehicle_type.lower() == "bike":
            return Bike()
        elif vehicle_type.lower() == "truck":
            return Truck()
        else:
            raise ValueError("Invalid vehicle type")


vehicle = VehicleFactory.create_vehicle("car")
print(vehicle.drive())