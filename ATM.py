class Atm:
    def __init__(self, cardnum,pin):
        self.cardnum = cardnum
        self.pin = pin

    def withdraw(self, money):
        balance = 5000000-money
        print("The remaining balance is " + str(balance))
    def checkBalance(self):
        print("Your current balance is 5000000") 

def main():
    cardnum = input ("Enter your cardnum ")
    pin = input ("Enter your pin ")
    Vaishnavi = Atm(cardnum,pin)
    print("Choose the activity")
    print("1. balance check")
    print("2. money withdraw")
    activity = int(input("Enter activity number"))
    if(activity == 1):
        Vaishnavi.checkBalance()
    elif(activity == 2):
        money = int(input("Enter the money "))
        Vaishnavi.withdraw(money)
    else:
        print("Invalid transaction")
if __name__ == "__main__":
    main()