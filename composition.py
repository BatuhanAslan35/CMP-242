class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Wheel:
    def __init__(self,size):
        self.size = size

class Car:
    def __init__(self, make, brand, horsepower, wheel_size):
        self.make = make
        self.brand = brand
        self.horsepower = Engine(horsepower)
        self.wheels = [Wheel(wheel_size) for _ in range(4)]
    
    def get_car(self):
        hp = self.horsepower.horsepower
        wheel_sizes = [wheel.size for wheel in self.wheels]
        return f"make = {self.make}, brand = {self.brand}, horsepower = {hp}, wheel size = {wheel_sizes}"
    


car1 = Car("toyota","corolla",120, 16)
print(car1.get_car())


