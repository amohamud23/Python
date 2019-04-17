class Person(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getname(self):
        return self.name
    
    def getage(self):
        return self.age

class Student(Person):
    
    def __init__(self, Person):
        self.age = Person.age
        self.name = Person.name

    def isStudent(self):
        return True

s = Person("Abdi",25)
u = Person("Bob", 21)

t = Student(s)
w = Student(u)

print(t.age, t.isStudent)
print(w.name, w.age)

