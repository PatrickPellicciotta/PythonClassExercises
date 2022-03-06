# create a class called Course. it should contain
# a title
# a course_id
# start an empty list of students
# a method to add a student to the list of students

from student import Student


class Course:
    def __init__(self, title, course_id):
        self.title = title
        self.course_id = course_id
        self.students = []

    def add_student(self, name, student_id):
        self.students.append(Student(name, student_id))

    def __str__(self):
        out = ''
        for s in self.students:
            out += str(s)+'\n'
        return out

