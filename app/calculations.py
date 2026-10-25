

class BackAccount():
    def __init__(self,startingPoint=0):
        self.balance=startingPoint
    def Deposit(self,amount):
        self.balance=+amount
    def Withdraw(self,amount):
        if amount>self.balance:
            raise Exception("you donot have enough balance")
        self.balance=self.balance-amount





def sum(x:int,y:int):
    return x+y

def subtract(x:int,y:int):
    return x-y

def multiply(x:int,y:int):
    return x*y

def divide(x:int,y:int):
    return x/y