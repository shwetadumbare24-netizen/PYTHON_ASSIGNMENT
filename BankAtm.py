class BankAtm:
    def __init__(self):
        self.pin = " "
        self.balance = 0

         
    def Menu(self):
        print("1 . Enter 1 to Create/set pin:")
        print("2 . Enter 2 to Check Balance:")
        print("3 . Enter 3 to Deposit Money:")
        print("4 . Enter 4 to withdraw Money:")
        print("5 . Enter 5 to Change Pin:")
        print("6 . Enter 6 to exit:")

        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                self.set_pin()
            case 2:
                self.check_balance()
            case 3: 
                self.deposit_money()
            case 4:
                self.withdraw_money()
            case 5:
                self.change_pin()
            case 6:
                self.exit_menu()

    def set_pin(self):
        if self.pin == " ":
            input_pin = input("Enter your pin:")
            self.pin = input_pin
            print("Pin set successfully:",self.pin)
            self.Menu()
            
        else:
            print("Pin is already set.")
            self.Menu()
        
    def check_balance(self):
        userPin = input("Enter your pin:")
        if self.pin == userPin:
           print("Your Balance is:",self.balance)
           self.Menu()
        else:
            print("Invalid Pin")
            self.Menu()

    def deposit_money(self):
        userPin = input("Enter your pin:")
        if self.pin == userPin:
            input_amount = int(input("Enter Amount For Deposit:"))
            self.balance += input_amount
            print("Your Bank Balance Is:",self.balance)
            self.Menu()
        else:
            print("Invalid Pin")
            self.Menu()

    def withdraw_money(self):
            userPin = input("Enter your pin:")
            if self.pin == userPin:
                withdraw_amount = int(input("Enter Amount For Withdraw:"))
                if withdraw_amount <= self.balance:
                    self.balance -= withdraw_amount
                    print("Your Bank Balance is:", self.balance)
                    self.Menu()

                     
                else:
                    print("Insufficiant Fund")
                    self.Menu()
            else:
                print("Invalid Pin")
                self.Menu()
    
    def change_pin(self):
        oldPin = input("Enter your old Pin:")

        if oldPin == self.pin:
            newpin = int(input("Enter New Pin:"))
            self.pin = newpin
            print("Pin Updated:",self.pin)
            self.Menu()
        else:
            print("Old pin is not match:")
            self.Menu()

    def exit_menu(self):
        print("Thank You")

obj1 = BankAtm()
obj1.Menu()  