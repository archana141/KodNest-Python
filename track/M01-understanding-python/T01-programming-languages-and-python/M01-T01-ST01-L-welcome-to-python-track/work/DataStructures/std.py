class Student:
    name = "Rahul"
    age = 22
    marks = 75

    def study(self):
        print(f"{self.name} is studying {self.age} years")

    def play(self):
        print(f"{self.name} is playing {self.age} years")

s1 = Student()
print(s1.name) 
print(s1.age)
print(s1.marks)

s1.study()
s1.play()

class Student:
    #Constructors
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def study(self):
        print(f"{self.name} is studying {self.age} years")

    def play(self):
        print(f"{self.name} is playing {self.age} years")

s1 = Student("Rahul", 23, 78.5)
print(f"Name:{s1.name}\nAge:{s1.age}\nMarks:{s1.marks}")
s2 = Student("Shakthi", 24, 85.6)
print(f"Name:{s2.name}\nAge:{s2.age}\nMarks:{s2.marks}")

s1.study()
s1.play()

s2.study()
s2.play()