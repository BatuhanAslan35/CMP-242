class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.__name = name
        self.__gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # getter for name
    def get_name(self):
        return self.__name
    
    # getter for gpa
    def get_gpa(self):
        return self.__gpa
    
    # getter for info
    def get_info(self):
        return f"Name = {self.__name} | GPA = {self.__gpa}"
    
    #class method for counting the total number of students.
    @classmethod
    def get_count(cls):
        return f"There is a total number of {cls.count} students."
    
    #class method for calculating the average gpa, it gets total gpa and dividing it by the total student count.
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"