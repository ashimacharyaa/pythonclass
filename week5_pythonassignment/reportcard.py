#report card assignment by ashim acharya
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks)
    
    def grade(self):# checking conditions
        avg = self.average()
        if avg >= 80:
            return 'A'
        elif avg >= 60:
            return 'B' 
        elif avg >= 40:
            return 'C'
        else:
            return 'D'

    def  display(self):
        avg = self.average()
        status = 'Pass' if avg>=40 else 'Fail'
        print(f"{self.name} -- AVG: {self.average()} -- Grade: {self.grade()} -- {status}")

students_data = [
    ('Ashim', [96,98,100,97,99]),
    ('Hom Nath', [99,87,96,89,89]),
    ('Manogya', [99,97,96,99,95]),
]
for name,marks in students_data:
    Student(name, marks).display()

