from Student import student
from exercises import Course
from random import randint

def add_random_grades(s: student):
    s.add_random_grades(randint(60-100))

def main():
    oop = Course('OOP II', 'P02-001')
    oop.add_student('john', '0001')
    oop.add_student('brandon', '0002')
    oop.add_student('harry', '0003')

    for student in oop.add_student:
        for i in range(5):
            add_random_grades(student)
    print(oop)

if __name__=='__main__':
    main()