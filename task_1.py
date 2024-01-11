class BankAccount:
    bankids = [1, 12, 123, 1234, 12456, 123456789]
    password = 123


    def __init__(self, bname, id,pin):
        self.bank = bname
        self.id = id
        self.pin=pin
        self.balance=20000

        if (self.id in BankAccount.bankids):
            self.validate_account(self.id,self.pin)

    def validate_account(self, accid, pin):
        if (accid == self.id):
            if (pin == self.password):
                while(True):
                    print(f"welcome to {self.bank}")
                    k = int(input("1.balance enquiry \n 2.deposit \n 3.with draw \n 4.exit\n enter your option:"))
                    if (k == 1):
                        print(self.balance)
                    elif (k == 2):
                        self.deposit(self.id)
                    elif (k == 3):
                        a = int(input("enter the with draw amount:"))
                        self.with_draw(a)
                    else:
                        exit()






    def deposit(self, id):
        if (id == self.id):
            n=int(input("place the deposit amount "))
            self.balance=n+self.balance
        else:
            print("invalid id please re enter the id ")

    def check_bal(self):
        print(self.balance)

    def with_draw(self, amount):
        if (self.balance - amount >= 0):
            print(amount)
            self.balance = self.balance - amount
        else:
            print("insufficient balance ")


myaccount = BankAccount("sbi", 123456789,pin=123)



