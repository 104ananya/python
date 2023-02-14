class Mammal:
    def walk(self):
        print('walking')


class Cat(Mammal):
    pass


class Dog(Mammal):
    def bark(self):
        print("barking")


dog1 = Dog()
dog1.walk()
