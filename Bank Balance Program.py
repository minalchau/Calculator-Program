balance=0
def check_balance():
    print("total balance:",balance)
def deposit(amount):
    global balance
    balance=balance+amount
    amount=int(input("enter the amountto be deposit:"))
    print("deposit is successful and the balance in the acount is",balance)
def withdraw(amount):
    global balance
    amount=int(input("enter the amount to withdraw:"))
    if (amount<=balance):
        balance=balance-amount
        print("the withdraw is successful",balance)
    else:
        print("insufficient balance")
while True:
    choice=int(input("\enter choice:\n1.deposit cash\t2.withdraw cash \n3.check_balance\t4.exit"))
    match choice: 
        
        case 1:
            print("deposit cash")
            d_amt=int(input("enter amount to deposit:"))
            deposit(d_amt)
            
        case 2:
            print("withdraw cash")
            w_amt=int(input("enter amount to withdraw:"))
            withdraw(w_amt)
            
        case 3:
            print("check_balance")
            check_balance()
            
        case 4:
            print("exiting")
            break
            
        case _:
            print("invalid choice")
            
