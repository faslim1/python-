# a = [11,13,14,15,16,17,18,19,20,12]

# convert the list into two lists [11,13,14,15,16] and [17,18,19,20,12]
# b = []
# d = len(a)//2
# c = []
# for i in range(len(a)):
#     if i<d:
#         b.append(a[i])
#     else:
#         c.append(a[i])
# print(b)
# print(c)

   
# a = [11,1,100,-900,10,15,16]
# print('largest= ',max(a))
# print('smallest= ',min(a))

a = [11,1,100,-900,10,15,16]
largest = 0
smallest = 0 
for i in a:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
print(largest)
print(smallest)

# Functions
# block of code which is executed whem it is called
# to call a function -- function_name()
# to define a function --def function_name()

# structural programming-- coding without using functions
# functional programming-- solving by using functions 
 
def function():
    print('Hai my name is Faslim')
function()

def funct(a,b): #a and b are former parameters
    print(a-b)
funct(9,5) #9 and 5 are actual parameters

# types of arguments

# positional argument
def fullname(fname,lname):
    print(fname+' '+lname)
fullname('faslim','rahim')

# keyword argument
def fullname(fname,lname):
    print(fname+' '+lname)
fullname(fname='faslim',lname='rahim')

# default aargument

def add(a=0,b=0):
    print(a+b)
add()
add(6)
add(4,5)







