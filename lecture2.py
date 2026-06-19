# lists
# list is a collection of items which is ordered and changeable.it allows duplicate members
mylist = [1,2,3,4,5]
print(mylist)
# lists are ordered 
# list are indexed 0,1,2,3,4,5 and -1,-2-3,-4

list = [10,20,[200,300],30,40,50]
print(list)
# list(start:end:step)
print(list[1:4])
print(list[:5])
print(list[::-1])
print(list[0:])
print(list[-3])

# list are mutable
# list is dynamic
# strings are immutable
# list are nested a[b[0,1]]

print(list[2][0])

# to add elements to the list

# append(element)
# it adds elements to the end of the list

list2 = [5,10,15,20,25]
list2.append(30)
print(list2)

# extend() adds an iterable to the list
list2.extend([30,'faslim',35,40])
print(list2)
print('\n')


# remove() removes the first occurence of that element
list2.remove(5)
list2.remove('faslim')
list2.pop()
list2.pop(0)
print(list2)
print('\n')


# tuples
# tuples are immutable
# so tuples are not dynamic

t = [10,20,30,40,50,60]
print(t[3])
print(t[::2])
print(t[:5])
print(t[0:])
print('\n')

t = ['apple','banana','orange','pineapple']
for i in range(0,len(t)):
    print(i,t[i])

# check if nummber is prime or not