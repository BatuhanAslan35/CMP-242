import email
class Students:
    discount_amt = 200
    def __init__(self, first_name, last_name, tuition_fee):
        self.first_name= first_name
        self.last_name = last_name
        self.tuition_fee = tuition_fee
        self.email_address = first_name + '.' + last_name + '@std.kyrenia.edu.tr'

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def apply_discount(self):
        self.tuition_fee = int(self.tuition_fee - self.discount_amt)

    def __repr__(self):
        return "Students({}, {}, {})".format(self.first_name, self.last_name, self.tuition_fee)
    
    def __str__(self):
        return '{} - {}'.format(self.full_name(), self.email_address)
    
    def __add__(self, other):
        return self.tuition_fee + other.tuition_fee
    
k2020xxxx = Students('HTOO THANT', 'PAING', 16000)
k2020xxxx.apply_discount()
k2021xxxx = Students('Kerem', 'k', 16000)
k2021xxxx.apply_discount()
k2022xxxx = Students('BORA', 'AKIN', 16000)
print(k2020xxxx)
print(k2020xxxx + k2021xxxx)