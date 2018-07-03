class Animal(object):

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    def __str__(self):
        return self.name


# Uses parent's init method
class Cat(Animal):

    # Class variable shared among all instances of a class
    found_rats = False

    def speak(self):
        print("Meow!")


class Person(Animal):

    def __init__(self, name, age):
        Animal.__init__(name, age)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friend(self, friend):
        self.friends.append(friend)

    def speak(self):
        print("Hello!")


class Student(Person):

    def __init__(self, name, age, major=None):
        Person.__init__(name, age)
        self.major = major
