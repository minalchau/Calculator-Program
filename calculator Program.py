# calculator program def function:

def add(a,b):
    ans= a+b
    print("addition is=",ans)
def sub(a,b):
    ans = a-b
    print("subtraction is=",ans)
def mul (a,b):
    ans = a*b
    print("multiplication=",ans)
def div(a,b):
    ans=a/b
    print("division is=",ans)
    
while True:

    choice = int(input("\n please enter your choice:\n1.add\t2.sub\n2.mul\t2.div\n3.exit"))
    if choice == 1:
        fn=int(input("enter your number:"))
        sn=int(input("enter your second number:"))
        add(fn,sn)

    elif choice == 2:
        fn=int(input("enter your number:"))
        sn=int(input("enter your second number:"))
        sub(fn,sn)
    elif choice ==3:
        fn=int(input("enter your number:"))
        sn=int(input("enter your second number:"))
        mul(fn,sn)

    elif choice ==4:
        fn=int(input("enter your number:"))
        sn=int(input("enter your second number:"))
        div(fn,sn)

    elif choice == 5:
        fn=int(input("enter your number:"))
        sn=int(input("enter your second number:"))
        print('exiting')
        break
    else:
        print('invalid choice')
