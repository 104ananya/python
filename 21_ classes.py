# object are instance of the class
class Point:

    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


# point1 = Point()
# point1.x = 10
# point1.y = 50
#
# print(point1.x)
# point1.draw()

point2 = Point(5, 7)
point2.x = 12
print(point2.x)


class Person:

    # constructor
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name} talking')


john = Person("John Smith")
print(john.name)
john.talk()