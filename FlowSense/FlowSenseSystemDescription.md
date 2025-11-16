# FlowSense: Intelligent Traffic Monitoring and Alert System

## Project Overview
FlowSense is a software system that simulates urban traffic flow and generates alerts based on certain conditions. 
The system collects speed and density data through sensor objects, analyzes it, and identifies potential risk situations. 
This project is designed to demonstrate object-oriented programming concepts in a realistic scenario for an OOP II course.

The system does not require games or physical sensors; all data is generated via object-based simulation.

---

## Main Classes and Functions

### Example Classes
- **SpeedSensor**
  - **collect_data()**: Simulates vehicle speeds in the zone.
  - **detect_stalled_vehicle()**: Detects vehicles that remain stationary for a certain time.
- **DensitySensor**
  - **collect_data()**: Simulates the number of vehicles in the zone.
  - **detect_accident_risk()**: Determines potential accident risks using density and speed data.
- **TrafficZone**
  - **collect_all_data()**: Collects data from all sensors in the zone.
  - **analyze_zone()**: Calculates average speed, vehicle density, and risk status.

…and other classes of this kind handle alerts, logging, and system management.

---

## Contributions
- Simulation of urban traffic flow.
- Detection of potential accident and congestion risks.
- Demonstration of object-oriented design principles.
- Modular and extensible system design.
- Data simulation without requiring real sensors or a game environment.

---

## Example Class Hierarchy
SpeedSensor, DensitySensor, TrafficZone, etc. → AlertSystem → FlowSenseSystem
