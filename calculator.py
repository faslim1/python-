# functions pt 2

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

def main():
    while True:
        print('-----Welcome to my Calculator-----')
        ch = int(input('\n1.ADD\n2.SUB\n3.MUL\n4.DIV\n5.EXIT\n----'))
        x = int(input('Enter your number:'))
        y = int(input('Enter your number:'))
        if ch==1:
            print(add(x,y))
        elif ch==2:
            print(sub(x,y))
        elif ch==3:
            print(mul(x,y))
        elif ch==4:
            print(div(x,y))
        elif ch==5:
            break
        else:
            print('Invalid Choice')
main()

 
