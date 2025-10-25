from student import Student
from studentstatus import StudentStatus

#creating objects
student1 = Student("Thoo", 3.9)
student2 = Student("Kerem", 4.0)
student3 = Student("Batu", 4)
student4 = Student("Max", 2)
student5 = Student("James", 3)
studentstatus1 = StudentStatus("ahmed", 1.9)

#calling functions from Student class
print(student1.get_info())
print(student2.get_info())
print(Student.get_count())
print(Student.get_average_gpa())

#prints passed or failed by checking the get_status function results from studentstatus class
if studentstatus1.get_status() == 1:
    print(f"{studentstatus1.get_name()} has passed!!")
else:
    print(f"{studentstatus1.get_name()} has failed!!")

#calling function from studentstatus class
print(studentstatus1.get_average_gpa())
