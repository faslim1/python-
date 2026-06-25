# nested loops

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,4):
#             print(i,j,k)

for i in range(1,6): 
    for j in range(6-i): 
        print(' ',end='')
    for k in range(1,i+1):
        print('* ',end='') #for printing stars

    print()

-----*
----**


for i in range(1,6): 
    for j in range(): 
        print(' ',end='')
    for k in range(1,i+1):
        print('* ',end='') 


# chessboard pattern

for i in range(1,6):
    for j in range(1,6):
        if (i+j)%2==0:
            print('W ',end='')
        else:
            print('B ',end='')
    print()
    