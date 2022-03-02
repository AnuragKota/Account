class Atm(object):
    "ATM Account"

    def __init__(self,Card_Number,Pin_Number):
        self.Card_Number=Card_Number
        self.Pin_Number=Pin_Number

    def check_balance(self):
        print("Your Balance Is 10000")

    def Withdrawal(self,amount):
        new_amount=10000-amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount)) 

    def main():
        Card_Number = input("insert your card number:- ")
        Pin_Number = input("enter your pin number:- ")
        new_user = Atm(Card_Number ,Pin_Number)
        print("Choose your activity ")
        print("1.Balance Enquriy 2.withdrawl")
        activity = int(input("enter activity number :- "))

        if (activity == 1):
           new_user.check_balance()
        elif (activity == 2):
            amount = int(input("enter the amount:- "))
            new_user.withdrawl(amount)
        else:
            print("enter a valid number")

    if __name__ == "__main__":
     main()            