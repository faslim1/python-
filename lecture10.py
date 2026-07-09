# exceptions
# events that affects the execution of program

try:
    a = 5 
    b = 5
    print(a/b)
except Exception as e:
    print('you have an error',e)
print('mohan')

# try:
#     int(input('enter :-'))
#     b = 5
#     print(a/b)
# except ZeroDivisionError:
#     print('you cannot divide a number with zero')
# except ValueError:
#     print('chack value')
# except TypeError:
#     print('check type')
# finally:
#     print('it will always execute')


# class myerror(Exception):
#     pass
# name = 'das'
# if name== 'das':
#     print('name should not be das')


# a = 4444
# del(a)
# print(a)

file1 = open('data.txt','r')
print(file1.read())
file1.close()

file2 = open('myfile.txt','w')
print(file2.write('hello everybody :)'))
file2.close()

file3 = open('myfile.txt','a')
file3.write('\nsuiiiiii!!')
for i in range(1,50):
    file3.write('\nronaldooo')
file3.close()

import os
# os.mkdir('images')  
# os.remove('data.txt') 
# os.rename('myfile.txt','demo.txt')

# pat = 
# if

