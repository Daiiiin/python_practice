class Vehicle:
    def __init__(self, vehicle_type, brand, model):
        self.vehicle_type = vehicle_type
        self.brand = brand
        self.model = model

    def display_vehicle(self):
        if self.vehicle_type == "Car":
            print("You car details: ")
        elif self.vehicle_type == "Motorcycle":
            print("You motorcycle details: ")

        print("Vehicle type: " + self.vehicle_type)
        print("Vehicle brand: " + self.brand)
        print("Vehicle model: " + self.model)


class Car(Vehicle):
    def __init__(self, car_brand, car_model):
        self.car_brand = car_brand
        self.car_model = car_model
        super().__init__("Car", car_brand, car_model)


class Motorcycle(Vehicle):
    def __init__(self, motor_brand, motor_model):
        self.motor_brand = motor_brand
        self.motor_model = motor_model
        super().__init__("Motorcycle", motor_brand, motor_model)


while True:
    v_type = input("What type of vehicle do you have (Car/Motorcycle)? ").lower()
    if v_type == "car":
        brand = input("What is your car brand? ")
        model = input("What is your car model? ")
        vehicle = Car(brand, model)
        break
    elif v_type == "motorcycle":
        brand = input("What is your motorcycle brand? ")
        model = input("What is your motorcycle model? ")
        vehicle = Car(brand, model)
        break
    else:
        print("Invalid vehicle type.")

vehicle.display_vehicle()