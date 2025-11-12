# Simulates and analyzes vehicle density in its zone.
class DensitySensor:
    
    def __init__(self, zone_id, zone_capacity=50):
        self.zone_id = zone_id
        # Assume a maximum capacity for this zone
        self.zone_capacity = zone_capacity

    # Returns the number of vehicles (density) in the zone.
    def collect_data(self, vehicles):
        return len(vehicles)

    # Calculates the density as a percentage.
    def get_density_percent(self, vehicle_count):
        if self.zone_capacity == 0:
            return 0
        return (vehicle_count / self.zone_capacity) * 100

    # Determines accident/congestion risk based on density and speed.
    def detect_accident_risk(self, vehicle_count, avg_speed):
        density_percent = self.get_density_percent(vehicle_count)
        
        # High density and low speed = congestion
        if density_percent > 80 and avg_speed < 15:
            return "HIGH RISK: Severe Congestion Detected!"
        # Medium density and low speed = heavy traffic
        elif density_percent > 60 and avg_speed < 30:
            return "MEDIUM RISK: Heavy Traffic and Slowdown."
        # High density and high speed = dangerous
        elif density_percent > 70 and avg_speed > 60:
            return "HIGH RISK: Increased Accident Probability (Fast and Dense)!"
        
        # No significant risk
        return None