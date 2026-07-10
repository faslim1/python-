# object oriented programming
# objects
# real life entity

# 2
# attributes - define an object
# behaviours  / methods

# class - blueprint
# to create objects

# methods - functions inside a class

# class car:
#     def start():
#         print('Car has started')
#     def stop():
#         print('Car has stopped')
# c1 = car
# c2 = car
# c3 = car
# c1.start()
# c2.stop()

# class bike:
#     def start():
#         print('bike has started')
#     def stop():
#         print('bike has stopped')
# b1 = 



# constructor - used to initialize an object
# represented by __init__


class car:
    def __init__(self,n,c):
        self.name = n
        self.colour = c
    def start(self):
        print(f'{self.name} with {self.colour} colour has started')
    def stop(self):
        print(f'{self.name} with {self.colour} colour has stopped')
    
c1 = car('swift','black')
c2 = car('city','blue')
c2.start()
c1.stop()

# create a class student
# with 6 attributes name,m1,m2,m3,m4,m5

# 3 methods

# sum of marks()
# average of marks()
# display()


class student:
    def __init__(self,name,m1,m2,m3,m4,m5):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5

    def sum(self):
        return self.m1+self.m2+self.m3+self.m4+self.m5
    def average(self):
        return (self.m1+self.m2+self.m3+self.m4+self.m5)/5
    def display(self):
        print(f'student has marks of {self.m1}, {self.m2},{self.m3},{self.m4},{self.m5} and the sum of marks is {self.sum()} and the average is {self.average()}')
        
std1 = student('john',10,15,20,25,30)
print(std1.sum())
print(std1.average())
print(std1.display())



# quiz game  with a timer (assignment)
