import datetime

# Logs simulation events to a .txt file.
class TrafficLogger:
    
    def __init__(self, filename="traffic_log.txt"):
        self.filename = filename
        # Clear the file on start and add a header
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.write(f"--- FlowSense Traffic Log Initialized: {datetime.datetime.now()} ---\n\n")
        except IOError as e:
            print(f"ERROR: Could not create log file {self.filename}: {e}")

    # Private method for writing log entries.
    def _log(self, message):
        try:
            # Open in 'append' mode to add to the file
            with open(self.filename, 'a', encoding='utf-8') as f:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{timestamp}] {message}\n")
        except IOError as e:
            print(f"ERROR: Could not write to log file: {e}")

    # Logs when a vehicle enters a zone.
    def log_vehicle_entry(self, vehicle, zone_id):
        self._log(f"[ZONE: {zone_id}] [ENTRY] {vehicle}")

    # Logs when an alert is generated.
    def log_alert(self, alert_message, zone_id, level="ALERT"):
        self._log(f"[ZONE: {zone_id}] [{level.upper()}] {alert_message}")