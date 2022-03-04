# create a class called Course. it should contain
# a title
# a course_id
# start an empty list of students
# a method to add a student to the list of students

from Student import student

class Course:
    def __init__(self, title, course_id):
        self.title = title
        self.course_id = course_id
        self.students = []

    def add_student(self, name, id):
        self.students.append(student(name, id))

    def __str__(self):
        out = ''
        for s in self.students:
            out += str(s)+'\n'
        return out

