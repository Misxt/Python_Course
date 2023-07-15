import random
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def solve_test(self):
        grade = (random.randint(0,100))
        if grade < 70:
            grade = grade + 30
        self.grades.append(grade)


    def get_average_grade(self):
        accumulator = 0
        for i in range(len(self.grades)):
            accumulator = accumulator + self.grades[i]
        return round(accumulator / len(self.grades))

Asa = Student("Asa")
Luciano = Student("Luciano")

class Classroom:
    def __init__(self, subject):
        self.subject = subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        print(self.subject)
        for i in range(len(self.students)):
            print(self.students[i].name)

    def test(self):
        for i in range(len(self.students)):
            self.students[i].solve_test()

    def get_approved_students(self):
        approved_students = []
        for i in range(len(self.students)):
            if self.students[i].get_average_grade() >= 70:
                approved_students.append(self.students[i].name)
        return approved_students
    
    def get_failed_students(self):
        failed_students = []
        for i in range(len(self.students)):
            if self.students[i].get_average_grade() <= 70:
                failed_students.append(self.students[i].name)
        return failed_students

math = Classroom("Math")
math.add_student(Asa)
math.add_student(Luciano)

for i in range(10):
    math.test()

print(f"{math.get_approved_students()} passed")
print(f"{math.get_failed_students()} failed")