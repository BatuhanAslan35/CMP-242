# Simulates and analyzes speed data for vehicles in its zone.
class SpeedSensor:
    
    def __init__(self, zone_id):
        self.zone_id = zone_id

    # Calculates the average speed from a list of vehicles.
    def collect_data(self, vehicles):
        if not vehicles:
            return 0
        total_speed = sum(v.speed for v in vehicles)
        return total_speed / len(vehicles)

    # Detects vehicles moving below a certain speed threshold (stalled).
    def detect_stalled_vehicle(self, vehicles, stall_threshold=5):
        # Return a list of vehicles that are considered stalled
        stalled_vehicles = [v for v in vehicles if v.speed < stall_threshold]
        return stalled_vehicles