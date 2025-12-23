# FlowSense: Intelligent Traffic Monitoring System

FlowSense is a modular, object-oriented Python library designed to simulate urban traffic flow, analyze density data, and generate risk alerts. It serves as a comprehensive implementation of advanced OOP principles, design patterns, and modern software packaging standards.

---

## 👨‍💻 Project Contribution & Development Workflow

> **Transparency Note:** This project represents a collaborative development process where the core implementation belongs to the student, supported by AI tools for optimization and structuring.

### 🧠 Lead Developer: **Batuhan Aslan**
**Batuhan** is the primary author of the codebase. His contributions include:
* **Core Implementation:** Wrote the fundamental logic for the `Vehicle`, `TrafficZone`, and `AlertSystem` classes.
* **Algorithm Design:** Developed the mathematical logic for calculating average speeds, density percentages, and accident risk probabilities.
* **System Architecture:** Designed the class hierarchy and relationships (Composition over Inheritance) as visualized in the UML diagrams.
* **Simulation Logic:** Constructed the main simulation loop and the interaction flow between zones and the central system.

### 🤖 Development Assistant: **Gemini AI**
**Gemini** acted as a technical consultant and refactoring tool. Its contributions were limited to:
* **Refactoring:** Assisting in decoupling the `TrafficAnalyzer` from sensors to adhere to the *Single Responsibility Principle (SRP)*.
* **Packaging Support:** Generating the standard `setup.py` and `__init__.py` boilerplate to convert the scripts into an installable Python package.
* **Debugging:** Identifying and resolving specific `ModuleNotFoundError` issues during the modularization phase.

---

## 📚 OOP II Concepts Applied (Course Syllabus Mapping)

This project has been engineered to demonstrate every concept covered in the OOP II curriculum:

### 1. Review of OOP I
* **Encapsulation:** All critical data (e.g., `self.vehicles` list in `TrafficZone`) is encapsulated. Access is controlled via methods, not direct modification.
* **Abstraction:** The `FlowSenseSystem` provides a high-level interface (`run_simulation_step`), hiding the complex complexity of sensor measurements and data analysis occurring inside each zone.

### 2. Static/Class Methods & Class Variables
* **Class Variables:** We utilized `_vehicle_counter` in the `TrafficZone` class. This variable is shared across all instances to ensuring every vehicle generated in the simulation gets a unique, sequential ID (e.g., VEH-1, VEH-2).

### 3. Operator Overloading (Special Methods)
* **`__str__`:** The `Vehicle` class implements the `__str__` magic method. This allows us to pass a vehicle object directly to the print function or logger (e.g., `logger.log(vehicle)`), resulting in a readable string representation automatically.

### 4. Composition vs. Inheritance
* **Design Choice:** The project strictly follows **Composition over Inheritance**.
* **Implementation:** As seen in our UML diagrams, a `TrafficZone` *IS NOT* a Sensor. Instead, it *HAS* a `SpeedSensor` and *HAS* a `DensitySensor`. This makes the system flexible and easier to maintain.

### 5. Exception Handling
* **Robustness:** The `TrafficLogger` class wraps file I/O operations in `try...except` blocks. This ensures the simulation does not crash if the log file is currently open by another program or if there are permission errors.

### 6. File Handling & Object Persistence
* **Logging:** The system implements a persistent log via `TrafficLogger`. It creates and appends to a `traffic_log.txt` file, recording every vehicle entry and risk alert with precise timestamps.

### 7. Iterators and Generators
* **Iterators:** The `TrafficZone` class implements `__iter__`. This allows the system to loop directly over a zone object (`for vehicle in zone:`) to update speeds, making the code cleaner.
* **Generators:** A custom generator using the `yield` keyword manages vehicle creation. Instead of creating a massive list of cars at once, it generates traffic "waves" on demand, simulating realistic flow.

### 8. Design Patterns
* **Singleton Pattern:** Applied to the `TrafficLogger` class. We used `__new__` to ensure that only **one** logger instance exists, preventing file access conflicts.
* **Factory Pattern:** Applied via `SensorFactory`. The `TrafficZone` does not instantiate specific sensor classes directly; it asks the factory to create them, adhering to the Open/Closed Principle.

### 9. Packaging and Modularization
* **Modular Structure:** The code is separated into logical modules (`vehicle.py`, `traffic_zone.py`, etc.) inside a dedicated `flowsense/` package directory.
* **Installability:** A `setup.py` file is included, allowing the entire project to be installed as a standard library using `pip install .`.

---

## 📦 Installation & Usage

**To install the library:**
```bash
pip install .
