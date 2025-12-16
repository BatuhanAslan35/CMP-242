from .speed_sensor import SpeedSensor
from .density_sensor import DensitySensor

# Implements Factory Pattern: Centralizes sensor creation logic.
class SensorFactory:
    
    @staticmethod
    def create_sensor(sensor_type, zone_id, capacity=None):
        """
        Factory method to create sensors based on type string.
        """
        if sensor_type == "speed":
            return SpeedSensor(zone_id)
        
        elif sensor_type == "density":
            if capacity is None:
                raise ValueError("Capacity is required for DensitySensor")
            return DensitySensor(zone_id, capacity)
            
        else:
            raise ValueError(f"Unknown sensor type: {sensor_type}")