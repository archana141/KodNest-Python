class Student:
    # Constructer
    def __init__(self, name, age, company):
        # Instance attributes - self or obj ref
        self.name = name
        self.age = age
        self.company = company

    #Instance method - using self reference, obj ref
    def study(self):
        # a = 10 # Loacal attributes
        # print(a)
        print(f"{self.name} is studying")

    def getDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("company:", self.company)
    
    def trip(self):
        print(f"{self.name} goes for a trip")

s1 = Student("Rahul", 20, "Kodnest")
s1.study()
s1.getDetails()

print("\n")
s2 = Student("Priya", 22, "Kodnest")
print(s2.name)
s2.study()
s2.getDetails()