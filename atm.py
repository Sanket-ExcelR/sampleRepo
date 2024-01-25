import random
class ATMSystem():
    all_accounts = []

    def __init__(self):
        self.name = ''
        self.opbal = 0
        self.uid = 0

    def create_ac(self):
        self.name = input("Enter Your Name: ")
        self.opbal = int(input("Enter Ac opening Balance: "))
        self.uid = random.randint(1000, 9999)
        print("Your Secret ID is {}".format(self.uid))
        self.all_accounts.append(self)

    def login(self):
        uid1 = int(input("Enter your ID: "))
        for account in self.all_accounts:
            if account.uid == uid1:
                print("Login successful!".center(100, "*"))
                return account
        print("Invalid ID".center(100, "*"))
        return None

    def l_choice(self):
        print("MENU".center(100, "-"))
        print("1. Withdraw".center(100,"."))
        print("2. Deposit".center(100,"."))
        print("3. Check Balance".center(100,"."))
        print("4. Logout".center(100,"."))
        print("".center(100, "-"))

    def withdraw(self):
        amt = int(input("Enter Amount to be Withdrawn: "))
        if amt > self.opbal:
            print("Insufficient Funds".center(100, "="))
            print("Available Balance: Rs.{}/-".format(self.opbal).center(100, "-"))
        else:
            self.opbal -= amt
            print("Withdrawal of {} is Successful".format(amt))
            print("Available Balance: Rs.{}/-".format(self.opbal))
            print("".center(100, "="))

    def deposit(self):
        depamt = int(input("Enter Amount to be Deposited: "))
        if depamt <= 0:
            print("Invalid amount. Please enter a valid amount.")
            return
        self.opbal += depamt
        print("Rs.{}/- Deposited Successfully!".format(depamt).center(100))
        print("Available Balance: Rs.{}/-".format(self.opbal).center(100))
        print("".center(100, "="))

    def ac_info(self):
        print("A/c holder Name: {}".format(self.name).center(100))
        print("Account Balance: Rs.{}/-".format(self.opbal).center(100))
        print("".center(100, "="))


def choice():
    print("1. Create Account".center(100))
    print("2. Login Account".center(100))
    print("3. Total Account".center(100))
    print("4. Total Balance".center(100))
    print("5. Exit".center(100))

obj = ATMSystem()

def operations(obj):
    while True:
        obj.l_choice()
        fch = int(input("Enter Choice: "))
        if fch == 1:
            obj1 = obj.login()
            obj1.withdraw()
        elif fch == 2:
            obj.deposit()
        elif fch == 3:
            obj.ac_info()
        elif fch == 4:
            print("Logged out Successfully!".center(100, "-"))
            break
        else:
            print("Please enter a valid input!".center(100, "-"))

print("Welcome To ATM".center(100, "-"))
while True:
    choice()
    try:
        ch = int(input("Enter Choice: "))
        if ch == 1:
            obj.create_ac()
        elif ch == 2:
            obj.login()
            operations(obj)
        elif ch == 3:
            print("Total Accounts: {}".format(len(ATMSystem.all_accounts)))
        elif ch == 4:
            total_balance = sum(account.opbal for account in ATMSystem.all_accounts)
            print("Available Funds in Bank: Rs.{}/-".format(total_balance))
        elif ch == 5:
            break
        else:
            print("Please enter a valid input!".center(100, "-"))
    except ValueError:
        print("Invalid input. Please enter a valid choice.")