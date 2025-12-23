# CMP-242: Object-Oriented Programming 2 – My Work So Far

This document summarizes my activities and learning in **CMP-242: Object Oriented Programming 2** during the first semester of the second year. It presents the exercises and in-class applications I have completed so far, as well as the implementation details of my term project, **FlowSense**.

## 📚 Topics Covered & Implemented

### Core OOP Principles
- **Composition over Inheritance** – Prioritizing "has-a" relationships (e.g., A Traffic Zone *has* Sensors) over "is-a" relationships to build more flexible systems.
- **Encapsulation & Abstraction** – Protecting internal object state and exposing only necessary interfaces to manage complexity.
- **Polymorphism** – Designing objects that share interfaces but behave differently based on context.

### Advanced Python Features
- **Iterators & Generators** – Implementing custom iterators (`__iter__`) and memory-efficient generators using the `yield` keyword for simulation loops.
- **Dunder (Magic) Methods** – Leveraging special methods like `__str__`, `__len__`, `__new__`, and `__init__` to integrate objects seamlessly with Python's built-in functions.
- **Class & Static Methods** – Utilizing `@staticmethod` for utility functions and class-level logic (e.g., in Factory classes).

### Software Architecture & Design Patterns
- **Design Patterns** – Implementing industry-standard solutions to common problems:
    - **Singleton Pattern:** Ensuring a single instance for the Logging system.
    - **Factory Pattern:** Centralizing object creation logic for Sensors.
- **Packaging & Modularization** – structuring code into a distributable Python package (`setup.py`, `__init__.py`) to support modularity and installation via `pip`.

### Robustness & Data Management
- **Exception Handling** – Implementing `try...except` blocks to manage runtime errors and ensure simulation stability (especially in File I/O).
- **File Handling** – Managing reading and writing operations for persistent logging mechanisms.
