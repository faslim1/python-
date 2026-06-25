#armstrong check

num = 153
sum = 0
og_num = num
power = len(str(num))
while num>0:
    b=num%10
    sum=sum+b**power
    num=num//10
if sum==og_num:
    print('armstrong num')
else:
    print('not armstrong num')
print('\n')

# check if number is prime or not    

a = int(input('Enter the number: '))
if a>1:
    for i in range (2,a):
        if a%i==0:
            print(f'{a} is not a prime number')
            break
    else:
        print(f'{a} is a prime number')
else:
    print(f'{a} is not a prime number')






a = int(input('Enter the number: '))
if a==1:
    print('not a prime number')
else:
    
