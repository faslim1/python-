#check if a number is odd or even
a = 6
if a%2==0:
    print('even')
else:
    print('odd')
print('\n')

# check if a number is multiple of 5
if a%5==0:
    print('multiple')
else:
    print('not multiple')
print('\n')

# largest of two numbers
a = 7
b = 9
if a>b:
    print('a is largest no')
else:
    print('b is largest no')
print('\n')

# check if nummber is positive or negative or zero

a = 4
if a>0:
    print('positive no')
elif a<0:
    print('negative')
else: 
    print('zero')
print('\n')

#largest of three numbers
a = 10
b = 11
c = -100

if a>b and a>c:
    print('a is largest')
elif b>a and b>c:
    print('b is largest')
else:
    print('c is largest ')
print('\n')

# check if a number is multiple of 3 and 5

a = 11
if (a%3==0 and a%5==0):
    print('multiple')
else:
    print('not multiple')


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

# sum of digits in a number

num = 343
sum = 0
while num>0:
    b=num%10
    sum=sum+b
    num=num//10
print(sum)


#reverse of number
num = 565
rev = 0
while num>0:
    b=num%10
    rev=rev*10+b
    num=num//10
print(rev)

print('\n')


# factorial of 5

num = 5
fact = 1

while num>0:
    fact=fact*num
    num=num-1
print(fact)

print('\n')

    
#100 numbers sum
i = 1
sum = 0

for i in range(101):
    sum=sum+i
print(sum)

print('\n')


num = 5
fact = 1
for i in range(num):
    fact=fact*num
    num=num-1
print(fact)

# multiplication table of a number
num = 5
for i in range(1,11):
    print(f'{num} x {i} = {num*i}')

print('\n')

# average of a number

# count = int(input('Enter num count:'))
# sum = 0
# for i in range(count):
#     int(input('enter the num:-'))
#     sum=sum+num
# print(f'sum is {sum}')
# print(f'average is {sum/count}')
print('\n')



print('\n')


