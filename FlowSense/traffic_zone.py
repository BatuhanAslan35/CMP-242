import random
from vehicle import Vehicle
# Uses Factory Pattern to create sensors instead of direct instantiation
from sensor_factory import SensorFactory
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
        # FACTORY PATTERN: Use the factory to create sensors
        self.speed_sensor = SensorFactory.create_sensor("speed", self.zone_id)
        self.density_sensor = SensorFactory.create_sensor("density", self.zone_id, capacity)
        
        self.analyzer = TrafficAnalyzer()
        
        # Initialize the continuous traffic flow generator
        self.traffic_stream = self._traffic_flow_generator()

    # Makes the TrafficZone object iterable, allowing direct loops over vehicles.
    def __iter__(self):
        return iter(self.vehicles)

    # Allows using len() directly on the TrafficZone object.
    def __len__(self):
        return len(self.vehicles)

    # Generator function that yields traffic entry signals based on probability.
    def _traffic_flow_generator(self):
        while True:
            rand_val = random.random()
            
            # High density flow: burst of vehicles
            if rand_val < 0.1:
                # Yield multiple entry signals consecutively
                for _ in range(3):
                    yield True
            # Normal flow: single vehicle
            elif rand_val < 0.4:
                yield True
            # Low flow: no vehicle
            else:
                yield False

    # Adds a new vehicle to the zone.
    def _add_vehicle(self):
        if len(self.vehicles) < self.capacity:
            TrafficZone._vehicle_counter += 1
            new_vehicle_id = f"VEH-{TrafficZone._vehicle_counter}"
            new_vehicle = Vehicle(new_vehicle_id)
            self.vehicles.append(new_vehicle)
            
            # Log the entry event
            self.logger.log_vehicle_entry(new_vehicle, self.zone_id)

    # Removes a random vehicle from the zone.
    def _remove_vehicle(self):
        if self.vehicles:
            # Remove a random vehicle from the list
            self.vehicles.pop(random.randint(0, len(self.vehicles) - 1))

    # Runs one step of the simulation for this zone.
    def update_simulation(self):
        
        # Update speed for all vehicles using the class iterator
        for v in self:
            v.update_speed()
            
        # Determine vehicle entry using the generator stream
        should_add_vehicle = next(self.traffic_stream)
        if should_add_vehicle:
            self._add_vehicle()
        
        # Simulate random vehicle exit
        if random.random() < 0.2:
            self._remove_vehicle()

    # Collects data from all sensors, analyzes it, and returns a report.
    def analyze_zone(self):
        
        # Extract raw speeds using list comprehension over the object itself
        raw_speeds = [v.speed for v in self]
        
        # Calculate average speed using the sensor
        avg_speed = self.speed_sensor.calculate_average_speed(raw_speeds)
        
        # Measure vehicle count using the sensor
        vehicle_count = self.density_sensor.measure_count(self.vehicles)
        
        # Identify stalled vehicles using the analyzer
        stalled_vehicles = self.analyzer.identify_stalled_vehicles(self.vehicles)
        
        # Calculate density percentage
        density_percent = self.density_sensor.calculate_density_percentage(vehicle_count)

        # Evaluate accident risk using the analyzer
        accident_risk = self.analyzer.evaluate_accident_risk(density_percent, avg_speed)
        
        # Compile the report
        report = {
            "zone_id": self.zone_id,
            "vehicle_count": vehicle_count,
            "avg_speed": avg_speed,
            "density_percent": density_percent,
            "stalled_vehicles": stalled_vehicles,
            "accident_risk": accident_risk
        }
        return report
