# We're creating a simple Engine class
class Engine:
    def __init__(self, horsepower):
        # We're saving the horsepower value
        self.horsepower = horsepower


# We're creating a Wheel class
class Wheel:
    def __init__(self, size):
        # We're saving the wheel size
        self.size = size


# Now we're creating a Car class that uses Engine and Wheel together
class Car:
    def __init__(self, make, brand, horsepower, wheel_size):
        # We're saving basic car info like make and brand
        self.make = make
        self.brand = brand
        # We're creating an Engine object inside the Car
        self.horsepower = Engine(horsepower)
        # We're creating 4 Wheel objects (one for each wheel)
        self.wheels = [Wheel(wheel_size) for _ in range(4)]
    
    # This method returns info about the car
    def get_car(self):
        # We're getting the horsepower value from the Engine object
        hp = self.horsepower.horsepower
        # We're getting all wheel sizes from the list of Wheel objects
        wheel_sizes = [wheel.size for wheel in self.wheels]
        # We're returning a nice formatted string with all car details
        return f"make = {self.make}, brand = {self.brand}, horsepower = {hp}, wheel size = {wheel_sizes}"
    

# We're creating a new Car object with its details
car1 = Car("toyota", "corolla", 120, 16)
# We're printing out the car's information
print(car1.get_car())
