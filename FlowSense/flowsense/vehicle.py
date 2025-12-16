import random

# Represents a single simulated vehicle.
class Vehicle:
    
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        # Initialize the vehicle with a random starting speed (0-90 km/h)
        self.speed = random.randint(0, 90)

    # Updates the vehicle's speed to simulate realistic behavior.
    def update_speed(self):
        
        # 30% chance of speed change
        if random.random() < 0.3:
            # Higher probability of slowing down
            change = random.randint(-10, 5) 
            # Speed cannot drop below 0
            self.speed = max(0, self.speed + change)
        
    def __str__(self):
        # Returns a string representation of the vehicle
        return f"Vehicle(ID: {self.vehicle_id}, Speed: {self.speed} km/h)"