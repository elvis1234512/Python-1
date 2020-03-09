print('Welcome to OB BANK')
print('Enter correct username and pin to continue')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter Pin: ')
    if password=='1006' and username=='OTU':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1


class Bank_Account: 

    def __init__(self): 

        self.balance=0

        print("Welcome {} ".format(username))
    

    def deposit(self): 

        amount=float(input("Enter the amount you want to Deposite: $")) 

        self.balance += amount 

        print("\n Amount Deposited: $",amount) 

    def withdraw(self): 

        amount = float(input("Enter amount you want to Withdraw: ")) 

        if self.balance>=amount: 

            self.balance-=amount 

            print("\n You Withdrew: $", amount) 

        else: 

            print("\n Insufficient balance  ") 

    def display(self): 

        print("\n Available Balance = $",self.balance) 

  
# Driver code 

   
# creating an object of class 

s = Bank_Account() 

   
# Calling functions with that class object 
s.deposit() 
s.withdraw() 
s.display()


