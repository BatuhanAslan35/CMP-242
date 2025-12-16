import datetime

# Logs simulation events to a .txt file.
# Implements Singleton Pattern: Ensures only one Logger instance exists.
class TrafficLogger:
    
    _instance = None

    def __new__(cls, filename="traffic_log.txt"):
        # Check if an instance already exists
        if cls._instance is None:
            # Create the instance if it doesn't exist
            cls._instance = super(TrafficLogger, cls).__new__(cls)
            cls._instance.filename = filename
            cls._instance._initialize_file()
        return cls._instance

    def _initialize_file(self):
        """Initializes the log file (runs only once)."""
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