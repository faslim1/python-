# inheritance
# single level inheritance
# child class
# multi level inheritance

# class person1:
#     def __init__(self):
#             pass
#     def walk(self):
#           print('person can waalkk')
#     def smile(self):
#         print('person can smiiile')
# class person2(person1):
#     def __init__(self):
#         pass
#     def read(self):
#         print('person can read')
#     def write(self):
#         print('person can wrrite')

# p1 = person2()
# p1.walk()

print('\n')


# class person1:
#     def __init__(self):
#             pass
#     def walk(self):
#         print('person can walkk')
#     def smile(self):
#         print('person can smiile')
#     def speak(self):
#         print('person1 can speak')

# class person2(person1):
#     def __init__(self):
#         pass
#     def read(self):
#         print('person can readd')
#     def write(self):
#         print('person can wrriite')
#     def speak(self):
#         print('person2 can speak')

# class person3(person2):
#     def __init__(self):
#         pass
#     def cry(self):
#         print('person can cry')
#     def scream(self):
#         print('person can scream')
#     def speak(self):
#         print('person3 can speak')

# class person4(person3):
#     def __init__(self):
#         pass
#     def eat(self):
#         print('person can eat')
#     def run(self):
#         print('person can run')
#     def speak(self):
#         print('person4 can speak')
#         super().speak()

# p4=person4()
# p4.speak()

# class person4(person1,person2,person3):
#     def __init__(self):
#         pass
#     def sleep(self):
#         print('person can sleep')
    
#     def eat(self):
#         print('person can eat')
    
#     def speak(self):
#         print('person 4 can speak')
#         super().speak()

# p4 = person4()
# p4.speak()
# print()


# polymorphism

# operator overloading
# method overloading
# method overriding

class student():
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self,othr):
        return self.m1+othr.m1,self.m2+othr.m2
    def __sub__(self,othr):
        return self.m1-othr.m1,self.m2-othr.m2
    def __mul__(self, othr):
        return self.m1*othr.m1,self.m2*othr.m2
    def __gt__(self,othr):
        return self.m1>othr.m1,self.m2>othr.m2
s1 = student(5,4)
s2 = student(9,8)
print(s1 + s2)
print(s1-s2)
print(s1*s2)
print(s1>s2)

# method overloading

class A:
    def __init__(self):
        pass
    def hello(self):
        print('A helloo')

class B:
    def __init__(self):
        pass
    def hello(self):
        print('B hellooo')

b = b.hello()
b.hello()





