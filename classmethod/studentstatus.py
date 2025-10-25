from student import Student
class StudentStatus(Student):
    def __init__(self, name, gpa):
        super().__init__(name, gpa)

    #indicates whether a student has passed or failed (1 for passed, 0 for failed)
    def get_status(self):
        if self.get_gpa() >= 2:
            return 1
        else:
            return 0
        
    #polymorphism: same class method as the parent class, but this method also calls the cls.count method.
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f} And There Is {cls.count} Student"