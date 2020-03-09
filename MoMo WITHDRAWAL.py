
import random
saved_data={}
class Account:
    def __init__(self,balance):
        self.balance=balance
        self.max_withdrawal=2000
        self.amount_today=0
        self.withdrawals_today=0
        self.limit_a_day=4
        
    def pin(self):
        pin=input('enter pin here')
        print('Your pin is {}'.format(pin))

    def acc_id(self):
        acc_id= random.randint(99,9999)
        print('Your account id is {}'.format(acc_id))


    def getBalance(self):
        print( self.balance)
    
    def withdraw(self):
        can_withdraw=True
        amount=int(input('enter amount here:'))
        if amount>self.max_withdrawal:
             can_withdraw=False
             print('Your amount is greater than the maximum withdrawals for the day')
        if amount>self.balance:
             can_withdraw=False
             print('Your amount is greater than your balance')
             
        if amount+self.amount_today>=self.max_withdrawal:
             can_withdraw=False
             print('You have reached the amount you can withdraw for today')
             
        if self.withdrawals_today>=self.limit_a_day:
             can_withdraw=False
             print('Youve reached the limit for today')
             
        else:
             self.withdrawals_today+=1
             self.amount_today+=amount
             self.balance -= amount
             print('Your new balance is {}.'.format(self.balance)) 


    def deposit(self):
        amount=int(input('Enter the amount you want to deposit here'))
        new_bal=self.balance + amount
        print('Your new balance is {}'.format(new_bal))


def displayMenu():
    print('*'*50)
    print('\nWelcome to MOMO')
    print('\nChoose sn option')
    print('\nPress 1 to withdraw')
    print('\nPress 2 to deposit')
    print('\nPress 3 to quit\n')
    print('*'*50)

def withdraw():
    print('*'*50)
    print('\nEnter Amount to withdraw')
    print('*'*50)
    userOption = int(input(''))
    



def momoProgram():
    keepOn = True
    while keepOn:
    
        displayMenu()
        userOption = int(input('Enter an option\n'))
        a=Account(30000)
        if userOption == 1 :
            a.withdraw()
        elif userOption ==2 :
            a.deposit()
        else:
            keepOn = False
            print('*'*50)
            print('\nGoodbye\n')
            print('*'*50)



'''a=Account(30000)
a.pin()
a.acc_id()
a.deposit()
a.withdraw()
a.getBalance()'''




momoProgram()




