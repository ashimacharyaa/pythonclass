'''
class car:
    color='white'
    engine=1500
    model_year=2017
    def run():
        print("The car runs on petrol")

honda=car()
print("The color of car is",honda.color)
print("The modelyear of car is",honda.model_year)
print("The engine of car is",honda.engine)'''

class student:
    ''' student class with constructir'''

    def __init__(self, name, grade, student_id):
        '''
        constructor method, 'self' refers to instance'''
        self.name=name
        self.grade=grade
        self.student.id=student_id

    def display_info(self):
        '''method to display student information'''
        print(f"Student:{self.name}")
        print(f"ID:{self.student_id}")

