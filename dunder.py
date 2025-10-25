import email  # not really used here, but it's okay to leave it for now

# We're creating a Students class
class Students:
    # We're setting a class-level discount amount (applies to all students)
    discount_amt = 200

    # When we create a new student, this runs automatically
    def __init__(self, first_name, last_name, tuition_fee):
        # We're saving the student's first name
        self.first_name = first_name
        # We're saving the student's last name
        self.last_name = last_name
        # We're saving the student's tuition fee
        self.tuition_fee = tuition_fee
        # We're automatically generating an email address for the student
        self.email_address = first_name + '.' + last_name + '@std.kyrenia.edu.tr'

    # We're creating a method to return the student's full name
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    # We're creating a method that applies the discount to the tuition fee
    def apply_discount(self):
        # We're subtracting the discount amount from the tuition fee
        self.tuition_fee = int(self.tuition_fee - self.discount_amt)

    # This is how the object looks when we print it directly (developer view)
    def __repr__(self):
        return "Students({}, {}, {})".format(self.first_name, self.last_name, self.tuition_fee)
    
    # This is how the object looks when we print it in a user-friendly way
    def __str__(self):
        return '{} - {}'.format(self.full_name(), self.email_address)
    
    # We're defining what happens when we use the + operator between two Students
    def __add__(self, other):
        # We're adding up their tuition fees
        return self.tuition_fee + other.tuition_fee


# We're creating a few student objects and applying the discount to each
k2020xxxx = Students('HTOO THANT', 'PAING', 16000)
k2020xxxx.apply_discount()

k2021xxxx = Students('Kerem', 'k', 16000)
k2021xxxx.apply_discount()

k2022xxxx = Students('BORA', 'AKIN', 16000)

# We're printing out one student's info (this uses the __str__ method)
print(k2020xxxx)

# We're printing the sum of two students' tuition fees (uses __add__)
print(k2020xxxx + k2021xxxx)
