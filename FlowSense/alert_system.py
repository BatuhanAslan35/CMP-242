from traffic_logger import TrafficLogger

# Analyzes risk conditions and generates alerts.
class AlertSystem:
    
    def __init__(self, logger: TrafficLogger):
        self.logger = logger

    # Prints an alert to the console and logs it to the file.
    def generate_alert(self, message, zone_id, level="ALERT"):
        alert_text = f"--- ALERT: ZONE {zone_id} --- \n{message}\n"
        
        # Print to console
        print("*" * 30)
        print(alert_text)
        print("*" * 30)
        
        # Also write to the log file
        self.logger.log_alert(message, zone_id, level)