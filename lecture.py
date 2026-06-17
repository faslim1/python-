# string
from multiprocessing.resource_sharer import stop


name = 'mohan'
print(name)
print(type(name))
print('\n')

data = '''mohan's resume'''
print(data)
print('\n')

qte = '''gandhi once told that "say no to violence"'''
print(qte)
print('\n')

# escape sequence
qte = 'gandhi \n once told that\"say no to violence"'
print(qte)
print('\n')

qte = 'gandhi \\n once told that\"say no to violence"'
print(qte)
print('\n')

# raw string
qte = r'gandhi \\n once told that\"say no to violence"'
print(qte)

# type conversion/casting


 
# a = int(input('enter a number --'))
# b = int(input('enter another number --'))
# print(type(a))

# 

# a = float(input('enter a number --'))
# b = float(input('enter another number --'))
# print(a+b)

#string formatting

# name = 'mohan'
# age = 18
# married_status = False
# rating = 4.5

# print(f'my name is {name} and my age is {age} and my married status is {married_status} and my rating is {rating}')

# control statements

# loops
# to stop executionn cntl+c

i = 1
sum = 0 
while i<=10:
    sum=sum+i
    i=i+1
print(sum)
    

# sum of first 10 numbers

i = 1
esum = 0
osum = 0
while i<=100:
    if i%2==0:
        esum=esum+i
    else:
        osum=osum+i
    i=i+1

print(osum)          
print(esum)