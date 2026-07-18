# 1. plot the points on a cartesian plane which has 2 coordinates x and y. do the following

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f'Point coordinates: ({self.x}, {self.y})')

p1 = Point(3, 4)
p1.display() 

# 2.define a class point. its instance should have 2 attributes x and y. x and y default value must be zero

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        print(f'Point coordinates: ({self.x}, {self.y})')

p2 = Point()
p2.display()

# 3.define a method move(). this should change the values of x and y

class point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def display(self):
        print('the coordinates are : ({self.x}:{self.y})')

    def move(self,a,b):
        self.x = a
        self.y = b
    def xmove():

class point:
    def __init__(self):
        self.x = a
        self.y = b



# access modifier

from abc import ABC,abstractmethod
class animal(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def makes_sound(self):
        print('animal makes sound')
class dog(animal):
    def __init__(self):
        pass
    def makes_sound(self):
        print('woff woff')
d = dog()
d.makes_sound()

# function which enhances another function

# encapsulation









    
        