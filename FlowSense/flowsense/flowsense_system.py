from .traffic_zone import TrafficZone
from .alert_system import AlertSystem
from .traffic_logger import TrafficLogger

# The main class that manages all traffic zones and the alert system.
class FlowSenseSystem:
    
    def __init__(self):
        print("FlowSense System Initializing...")
        self.logger = TrafficLogger("traffic_log.txt")
        self.alert_system = AlertSystem(self.logger)
        
        # Let's create 2 different zones for the simulation
        self.zones = [
            TrafficZone("Zone-A (Highway)", self.logger, capacity=100),
            TrafficZone("Zone-B (City Center)", self.logger, capacity=40)
        ]
        print(f"{len(self.zones)} traffic zones are active.")

    # Runs a single 'step' (or tick) of the simulation.
    def run_simulation_step(self):
        
        print("\n--- Simulation Step Starting ---")
        
        for zone in self.zones:
            # 1. Update vehicles in the zone (speed change, entry/exit)
            zone.update_simulation()
            
            # 2. Analyze the zone
            report = zone.analyze_zone()
            
            # 3. Print the report
            print(f"[{zone.zone_id}] Report: {report['vehicle_count']} Vehicles, "
                  f"Avg. Speed: {report['avg_speed']:.1f} km/h, "
                  f"Density: {report['density_percent']:.1f}%")

            # 4. CHECK FOR ALERTS
            # Check for congestion/accident risk
            if report['accident_risk']:
                self.alert_system.generate_alert(
                    report['accident_risk'], 
                    zone.zone_id, 
                    level="RISK"
                )
                
            # Check for stalled vehicles
            if report['stalled_vehicles']:
                self.alert_system.generate_alert(
                    f"STALLED VEHICLE DETECTED! {len(report['stalled_vehicles'])} vehicles stopped.",
                    zone.zone_id,
                    level="EMERGENCY"
                )