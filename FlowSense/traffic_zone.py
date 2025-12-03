import random
from vehicle import Vehicle
from speed_sensor import SpeedSensor
from density_sensor import DensitySensor
from traffic_analyzer import TrafficAnalyzer
from traffic_logger import TrafficLogger

# Manages a specific urban area and its internal sensors.
class TrafficZone:
    
    # Shared vehicle ID counter for all zones
    _vehicle_counter = 0

    def __init__(self, zone_id, logger: TrafficLogger, capacity=50):
        self.zone_id = zone_id
        self.vehicles = []
        self.logger = logger
        self.capacity = capacity
        
        # OOP: Composition - The TrafficZone 'has-a' relationship with its sensors
        self.speed_sensor = SpeedSensor(self.zone_id)
        self.density_sensor = DensitySensor(self.zone_id, capacity)
        self.analyzer = TrafficAnalyzer()

    # Adds a new vehicle to the zone (simulation).
    def _add_vehicle(self):
        if len(self.vehicles) < self.capacity:
            TrafficZone._vehicle_counter += 1
            new_vehicle_id = f"VEH-{TrafficZone._vehicle_counter}"
            new_vehicle = Vehicle(new_vehicle_id)
            self.vehicles.append(new_vehicle)
            
            # Desired logging: Every entering vehicle is logged
            self.logger.log_vehicle_entry(new_vehicle, self.zone_id)

    # Removes a random vehicle from the zone (simulation).
    def _remove_vehicle(self):
        if self.vehicles:
            # Remove a random vehicle from the list
            self.vehicles.pop(random.randint(0, len(self.vehicles) - 1))

    # Runs one step of the simulation for this zone.
    def update_simulation(self):
        
        # 1. Update vehicle speeds
        for v in self.vehicles:
            v.update_speed()
            
        # 2. Simulate random vehicle entry/exit
        # 50% chance for a new vehicle to enter
        if random.random() < 0.5:
            self._add_vehicle()
        
        # 20% chance for a vehicle to leave
        if random.random() < 0.2:
            self._remove_vehicle()

    # Collects data from all sensors, analyzes it, 
    # and returns a report (dictionary).
    def analyze_zone(self):
        
        # Collect data from sensors
        # Extract raw speeds to pass to the sensor (Decoupling)
        raw_speeds = [v.speed for v in self.vehicles]
        
        avg_speed = self.speed_sensor.calculate_average_speed(raw_speeds)
        
        vehicle_count = self.density_sensor.measure_count(self.vehicles)
        
        # Analyze risks
        # Use TrafficAnalyzer to find stalled vehicles
        stalled_vehicles = self.analyzer.identify_stalled_vehicles(self.vehicles)
        
        # Get density percentage for the report
        density_percent = self.density_sensor.calculate_density_percentage(vehicle_count)

        # Use TrafficAnalyzer to evaluate accident risk
        accident_risk = self.analyzer.evaluate_accident_risk(density_percent, avg_speed)
        
        # Return the analysis result as a report
        report = {
            "zone_id": self.zone_id,
            "vehicle_count": vehicle_count,
            "avg_speed": avg_speed,
            "density_percent": density_percent,
            "stalled_vehicles": stalled_vehicles,
            "accident_risk": accident_risk
        }
        return report
