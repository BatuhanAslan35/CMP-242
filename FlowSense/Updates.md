# 📜 FlowSense Development Changelog

---

## 📅 03.12.2025 — Architectural Refactoring & SRP Compliance

### 🛠️ Decoupling Sensors from Vehicles

> **Feedback:** WHY WILL THE SENSOR DIRECTLY ACCESS (VEHICLE)? SENSOR SHOULD ONLY REPORT.

* **What I changed:** I realized that passing the whole Vehicle object to the sensor created a dependency that wasn't necessary. The sensor doesn't need to know the car's ID or other properties; it just needs the numbers.
* **The Fix:** I modified `traffic_zone.py` and `speed_sensor.py`. Now, instead of sending the list of vehicle objects to the sensor, I extract the speeds first (e.g., `raw_speeds = [v.speed for v in self.vehicles]`) and just send that list of integers. Now the sensor is strictly a measuring tool and doesn't "know" what a vehicle is.

### 🛡️ Safe Data Handling

> **Feedback:** BATUHAN, returning [0] MIGHT BE MISINTERPRETED AS ACTUAL DATA ESPECIALLY IF VEHICLES CONTAINS A NONE VALUES OR NON-VEHICLE, I SUGGEST YOU CONSIDER RETURNING AN EMPTY LIST []

* **What I changed:** You were right, returning `[0]` was risky because it looks like valid data (a car moving at 0 km/h) rather than "no data."
* **The Fix:** I went through `speed_sensor.py` and `traffic_analyzer.py`. I added checks like `if not vehicles: return []`. Now, if the road is empty or the list is null, the system explicitly returns an empty list `[]` or `0.0`. This prevents the system from confusing an empty road with a traffic jam.

### 🧠 Separation of Concerns (TrafficAnalyzer)

> **Feedback:** THE SENSOR SHOULD ONLY COLLECT DATA, NOT TO MAKE DECISIONS REGARDING THE REASON FOR A STALLED VEHICLE. THAT SHOULD BE DONE IN 'TrafficAnalyzer' CLASS.

* **What I changed:** I was violating the Single Responsibility Principle (SRP). My sensors were doing too much work—they were measuring and judging the situation.
* **The Fix:** I created a brand new class called `TrafficAnalyzer`.
    * **Old way:** The SpeedSensor decided if a car was "stalled."
    * **New way:** The SpeedSensor only calculates averages. I moved all the "decision" logic (detecting stalled cars, calculating accident risks) into TrafficAnalyzer. The TrafficZone now asks the Sensor for the numbers, and then asks the Analyzer what those numbers mean.

---

## 📅 07.12.2025 — Pythonic Enhancements

### ✨ Feature: Added Iterators and Generators to TrafficZone

* Made `TrafficZone` iterable using `__iter__`; we can now loop over the object directly without touching internal lists.
* Implemented a generator with `yield` to manage vehicle entry. This simulates realistic traffic waves (like rush hour bursts) and improves memory usage by generating flow states on demand.

---

## 📅 12.12.2025 — Design Patterns Implementation

### 🌟 Major Architecture Update: Design Patterns

Added **Singleton** and **Factory** design patterns to make the system more robust and scalable.

#### 1. Singleton Pattern (`TrafficLogger`)
* **Why?** We realized that having multiple logger instances could cause issues with the log file (like overwriting headers).
* **Change:** Modified `TrafficLogger` using `__new__` to ensure that only **one single instance** of the logger exists throughout the entire application lifecycle, no matter how many times we call it.

#### 2. Factory Pattern (`SensorFactory`)
* **Why?** The `TrafficZone` class was too tightly coupled to specific sensor classes (`SpeedSensor`, `DensitySensor`). If we wanted to add a `WeatherSensor`, we had to modify `TrafficZone`.
* **Change:** Created a `SensorFactory` class. Now `TrafficZone` just asks the factory for a "speed" or "density" sensor, and the factory handles the instantiation details. This improves **Encapsulation** and adheres to the **Open/Closed Principle**.
