# Simulates and analyzes speed data for vehicles in its zone.
class SpeedSensor:
    
    def __init__(self, zone_id):
        self.zone_id = zone_id

    # Calculates average speed from a list of raw speed values (integers/floats).
    def calculate_average_speed(self, speed_data_list):
        #Handle empty lists gracefully.
        if not speed_data_list:
            return 0.0
        
        total_speed = sum(speed_data_list)
        return total_speed / len(speed_data_list)
