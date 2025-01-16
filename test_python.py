# Parent Class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Vehicle Brand: {self.brand}, Model: {self.model}")

# Child Class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def display_car_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}, Doors: {self.doors}")

# Usage
car = Car("Toyota", "Corolla", 4)
car.display_info()  # Inherited method from Vehicle
car.display_car_info()  # Method in Car class