class Account:
    
    def __init__(self,name,balance,min_balance):
       
       self.name=name
       self.balance=balance
       self.min_balance=min_balance

    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print 'Sorry, not enough money in your Account'

    def statement(self):
        print ' Account balance: ${}'.format(self.balance)


class Current(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=-1000)
