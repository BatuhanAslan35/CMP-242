class TrafficAnalyzer:
    
    def __init__(self):
        pass

    # Identifies vehicles that are stopped.
    def identify_stalled_vehicles(self, vehicles, stall_threshold=5):
        # Returns a list of stalled vehicles.
        # we return an empty list [], not None or [0].
        if not vehicles:
            return []
            
        stalled = [v for v in vehicles if v.speed < stall_threshold]

        return stalled

    # Evaluates accident risk based on aggregated data.
    def evaluate_accident_risk(self, density_percent, avg_speed):
        
        if density_percent > 80 and avg_speed < 15:
            return "HIGH RISK: Severe Congestion Detected!"
            
        elif density_percent > 60 and avg_speed < 30:
            return "MEDIUM RISK: Heavy Traffic and Slowdown."
            
        elif density_percent > 70 and avg_speed > 60:
            return "HIGH RISK: Increased Accident Probability (Fast and Dense)!"
        
        return None