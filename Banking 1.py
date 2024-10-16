

class Customer:
    bankname = "XYZ Bank"
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("Balance After Deposit is ",self.balance)

    def withdraw(self,amount):
        if self.balance < amount:
            print("Can not Perform this Operation")
            print("Insufficient Fund")
        else:
            self.balance-=amount
            print("Balance After Withdraw is ",self.balance)


print("Welcome to ",Customer.bankname)
name = input("Enter Customer Name : ")
c1 = Customer(name)
while True:
    print("1. Deposit\n2. Withdraw\n3. Exit")
    option = int(input("Enter your Option"))
    if option == 1:
        amount = int(input("Enter the Amount for Deposit"))
        c1.deposit(amount)
    elif option == 2:
        amount = int(input("Enter the Amount for Withdraw"))
        c1.withdraw(amount)
    elif option == 3:
        print("Thanks for Banking with Us!!!")
        exit()
    else:
        print("Invalid Option")









        
