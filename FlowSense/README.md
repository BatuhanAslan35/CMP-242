1. WHY WILL THE SENSOR DIRECTLY ACCESS (VEHICLE)? SENSOR SHOULD ONLY REPORT.

What I changed: I realized that passing the whole Vehicle object to the sensor created a dependency that wasn't necessary. The sensor doesn't need to know the car's ID or other properties; it just needs the numbers.

The Fix: I modified traffic_zone.py and speed_sensor.py. Now, instead of sending the list of vehicle objects to the sensor, I extract the speeds first (e.g., raw_speeds = [v.speed for v in self.vehicles]) and just send that list of integers. Now the sensor is strictly a measuring tool and doesn't "know" what a vehicle is.

2. BATUHAN, returning [0] MIGHT BE MISINTERPRETED AS ACTUAL DATA ESPECIALLY IF VEHICLES CONTAINS A NONE VALUES OR NON-VEHICLE, I SUGGEST YOU CONSIDER RETURNING AN EMPTY LIST []

What I changed: You were right, returning [0] was risky because it looks like valid data (a car moving at 0 km/h) rather than "no data."

The Fix: I went through speed_sensor.py and traffic_analyzer.py. I added checks like if not vehicles: return []. Now, if the road is empty or the list is null, the system explicitly returns an empty list [] or 0.0. This prevents the system from confusing an empty road with a traffic jam.

3. THE SENSOR SHOULD ONLY COLLECT DATA, NOT TO MAKE DECISIONS REGARDING THE REASON FOR A STALLED VEHICLE. THAT SHOULD BE DONE IN 'TrafficAnalyzer' CLASS.

What I changed: I was violating the Single Responsibility Principle (SRP). My sensors were doing too much work—they were measuring and judging the situation.

The Fix: I created a brand new class called TrafficAnalyzer.

Old way: The SpeedSensor decided if a car was "stalled."

New way: The SpeedSensor only calculates averages. I moved all the "decision" logic (detecting stalled cars, calculating accident risks) into TrafficAnalyzer. The TrafficZone now asks the Sensor for the numbers, and then asks the Analyzer what those numbers mean.

# FlowSense: Intelligent Traffic Monitoring System

FlowSense is a software system that simulates urban traffic flow and generates alerts based on certain conditions. The system collects speed and density data through sensor objects, analyzes it, and identifies potential risk situations. This project was designed to demonstrate key object-oriented programming concepts for an OOP II course.

---

## Project Contribution Acknowledgement

> This FlowSense simulation system was developed as a collaborative effort.
>
> The core architectural design, data modeling, and class hierarchy were conceptualized and structured by **Batuhan Aslan**. This primary work included the definition and coding of all main classes, such as `TrafficZone`, `Vehicle`, `SpeedSensor`, `DensitySensor`, `AlertSystem`, and the `TrafficLogger` (which handles all file I/O operations). This formed the complete foundation of the object-oriented design.
>
> Assistance from the Gemini AI was utilized for specific implementation tasks and refinement. This support included helping to structure the main simulation `for` loop in `main.py` and refining the internal logic for some of the more complex interactions, such as the vehicle update simulation and the risk-detection rules.

---

## OOP II Concepts Applied

Here is a breakdown of how the OOP concepts from the course are applied within the FlowSense project:

### 1. Review of OOP I (Encapsulation, Abstraction)

* **Encapsulation:** This is demonstrated in nearly every class. For example, the `TrafficZone` class encapsulates its own list of `vehicles`. Other classes cannot access this list directly. Similarly, the `Vehicle` class encapsulates its `self.speed`, which is only modified internally by its own `update_speed()` method.
* **Abstraction:** This is a core principle. The `FlowSenseSystem` class is an abstraction. It operates on `TrafficZone` objects without needing to know the *internal details* of how a zone analyzes data. Likewise, the `TrafficZone` abstracts the sensors; it simply calls `speed_sensor.collect_data()` without knowing the complex calculations inside.
* **Inheritance & Polymorphism:** These concepts were not explicitly used, as we favored Composition.

### 2. Static/Class Methods & Class/Instance variables

* **Instance Variables:** These are used extensively. `self.zone_id` (in `TrafficZone`), `self.speed` (in `Vehicle`), and `self.logger` (in `AlertSystem`) are all instance variables, meaning each object gets its own unique copy.
* **Class Variables:** We have a clear example of a class variable in `TrafficZone`: the `_vehicle_counter`. This variable is shared across *all* instances of `TrafficZone` to ensure that every vehicle in the simulation gets a unique ID.
* **Static & Class Methods:** We did not use `@staticmethod` or `@classmethod` in this project.

### 3. Introduction to Operator Overloading (Special Methods)

* Yes, this concept is used. The `Vehicle` class implements the special method `__str__(self)`. This is a form of operator overloading that changes how the `str()` function or `print()` command behaves with a `Vehicle` object, allowing `TrafficLogger` to write a clean, readable string to the log file.

### 4. Composition vs Inheritance

* This is the **most important design principle** in the FlowSense project. We explicitly chose **Composition over Inheritance**.
* A `TrafficZone` *does not* inherit from `SpeedSensor`; instead, it *has-a* `SpeedSensor` and *has-a* `DensitySensor` as instance variables. This is a powerful, flexible design that allows for easy future expansion (e.g., adding a `WeatherSensor`).

### 5. Exception Handling

* This is demonstrated clearly in the `TrafficLogger` class. Both the `__init__` and `_log` methods are wrapped in `try...except IOError` blocks. This is a robust way to prevent the entire simulation from crashing if the `traffic_log.txt` file is locked or if the program lacks write permission.

### 6. File Handling & Object Persistence

* **File Handling:** This is the primary responsibility of the `TrafficLogger` class. It uses Python's built-in `open()` function in both write (`'w'`) mode (to initialize the log) and append (`'a'`) mode (to add new entries).
* **Object Persistence:** The project does *not* use full object persistence. We are *logging* the *string representation* of objects, not serializing the objects themselves (e.g., using `pickle` or `json.dump`) to reload the simulation state.
