from collections.abc import ValuesView
departments = [
    ["Asha","Ravi"],
    ["Meera","Kiran"],
    ["John","Sara"]
]

seats = [
    ["Asha","Ravi"],
    ["Meera","Kiran"]
]

student ={
    "name":"Asha",
    "subjects":["Python","SQL","Java"]
}

print(student)

students = {
    "name":"Asha",
    "marks":{
        "Python":88,
        "SQL":82,
        "Java":91
    }
}

students =[
    {
        "name":"Asha",
        "branch":"CSE"
    },
    {
        "name":"Ravi",
        "branch":"ECE"
    }
]
print(students)

students = [
    {
        "name": "Asha",
        "marks": [78,85,91]
    },
    {
        "name": "Ravi",
        "marks": [72,88,80]
    }
]

marks = [
    [78,85,91],
    [72,88,80]
]

student = {
    "name":"Asha",
    "skills":["Python","SQL"]
}
student = {
    "name":"Asha",
    "marks":{
        "Python":88,
        "SQL":82
    }
}

students_marks = [
    [78,85,91],
    [72,88,80],
    [90,84,89]
]

for marks in students_marks:
    for mark in marks:
        print(mark)

student_marks =[
    [78,85,91],
    [72,88,80]
]

for marks in student_marks:
    print(marks)

departments = {
    "Development":["Asha","Ravi"],
    "Testing":["Meera","Kiran"]
}

for department, employees in departments.items():
    print(department)
    for employee in employees:
        print(employee)

for department,employees in departments.items():
    for employee in employees:
        print(department,"-",employee)

student = {
    "Asha":{
        "Python":88,
        "SQL":82
    },
    "Ravi":{
        "Python":76,
        "SQL":84
    }
}

for students_name,marks in student.items():
    print(students_name)
    for subject,mark in marks.items():
        print(subject,mark)

students = [
    {
        "name":"Asha",
        "score":88
    },
    {
        "name":"Ravi",
        "score":82
    }
]

for student in students:
    print(student["name"],student["score"])

students =[
    {
        "name":"Asha",
        "marks":[78,85]
    },
    {
        "name":"Ravi",
        "marks":[72,88,80]
    }
]

for student in students:
    print(student["name"])
    for mark in student["marks"]:
        print(mark)

students =  [
    {
        "name":"Asha",
        "marks":[78,85,91]
    },
    {
        "name":"Ravi",
        "marks":[72,88,80]
    }
]

for student in students:
    total = 0
    for marks in student["marks"]:
        total += mark
    print(student["name"],total)

for student in students:
    total = 0
    for mark in student["marks"]:
        total += mark
    average = total / len(student["marks"])
    print(student["name"],average)
