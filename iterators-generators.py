'''
a = [1,4,5,9]
i = a.__iter__()
print(i)
try:
    print(next(i))
    print(i.__next__())
    print(i.__next__())
    print(i.__next__())
    print(i.__next__())
except StopIteration:
    print(f"There is only {len(a)} items in the list!")
'''


'''
a = [1,4,5,9,2,5]
i = a.__iter__()
for x in range(len(a)):
    print(next(i))
'''

'''
class skipIterator:
    def __init__(self, inList):
        self.__inner = inList.__iter__()
    def __iter__(self):
        return self
    def __next__(self):
        self.__inner.__next__()
        return self.__inner.__next__()
    
s = skipIterator([1,2,3,4,5,6,7,8,9,10])
for x in s:
    print(x)
    
'''

'''
cmp242=["Bora", "Judah", "Zait", "Akin"]
c_iter = iter(cmp242)
for students in c_iter:
    print(students)
'''

'''
cmp242 = []
def greeting_class(cmp242):
    for every_student in cmp242:
        print(f"Hello {every_student}")

greeting_class(["batu","voltage", "judah"])
greeting_class(("bora", "kerem", "Nurullah","mehmet"))
'''

'''

class ReverseIterator:
    def __init__(self,items):
        self.items = items
        self.index = len(items) - 1
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.items[self.index]
        self.index -= 1
        return value

a = [1,4,5,9]
for item in ReverseIterator(a):
    print(item)

'''
'''
class findDist:
    def __init__(self,tstr,char):
        self.string = tstr
        self.char = char
        self.pos = 0
    def __iter__(self):
        return self
    def __next__(self):
        delta = 0
        if (self.pos == len(self.string)):
            raise StopIteration()
        while (self.string[self.pos] != self.char):
            delta += 1
            self.pos += 1
        self.pos += 1
        return delta

for i in findDist('abracadabra', 'a'):
    print(i) 

'''

def findDistYield(string,char):
    delta = 0
    for c in string:
        if c ==char:
            yield delta
            delta = 0
        else :
            delta += 1

for i in findDistYield('abracadabra', 'a'):
    print(i)