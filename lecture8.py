# recursion
# 10 numbers

# def counttozero(n):
#     print(n)
#     if n == 0:
#         return
    
#     return n + counttozero(n-1)

# counttozero(10)
print('\n')


# sum

# def sum(n):
#     print(n)
#     if n == 0:
#         return

#     return  n + sum(n-1)

# sum(10)


# scope of a variable
# scope - area in which it is recognized
# LEGB
# local enclosing global bulit in

def myname():

    name = 'faslim' #global variable
    def nickname():
        name = 'yazin' #local variable

        print(name)
    # nickname()
    # print(name)

myname()

name = 'fffff'

num = int(input('enter number'))
fact = 1
for i in range(1,num+1):
    fact=fact*num
    num=num-1
print(fact)



