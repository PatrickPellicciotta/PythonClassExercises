'''
QUIZ #4
Name: Patrick Pellicciotta
ID: 2210211

Follow the instructions in the comments below. Then upload this file, with your answers, to Omnivox.
'''
# 1.  Create a class called Square with the following attributes:
# - Width (int)
# - Height (int)
# Your class should also have the following methods:
# - get_area    which takes in nothing and returns width * height
# - __str__     which takes in nothing and returns a string with the width, height, and area of the square
# - __gt__      which takes in another sqaure and compares them based on area
# - __ge__      which works like __gt__, except using greater ot equal
# - __eq__      which works like __gt__, except using equal


class Square:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return f"width {self.width} height {self.height} area {self.get_area()}"

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()


# 2. Create two squares, compare them, and print out the bigger one.

square1 = Square(20, 20)

square2 = Square(20, 20)

if square1 > square2:
    print(square1)
elif square2 > square1:
    print(square2)
elif square2 == square1:
    print("squares are equal in size")