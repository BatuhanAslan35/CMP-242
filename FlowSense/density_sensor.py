# density_sensor.py

# Responsible ONLY for measuring density. No decision making.
class DensitySensor:
    
    def __init__(self, zone_id, zone_capacity=50):
        self.zone_id = zone_id
        self.zone_capacity = zone_capacity

    # Returns the count of vehicles.
    def measure_count(self, vehicle_list):
        # Simply counts the list items
        return len(vehicle_list)

    # Returns density as a percentage.
    def calculate_density_percentage(self, current_count):
        if self.zone_capacity == 0:
            return 0.0

        return (current_count / self.zone_capacity) * 100
