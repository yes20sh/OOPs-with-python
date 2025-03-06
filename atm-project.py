class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    
    def menu(self):
        while True:
            option = input('''
        1 : Enter (1) to create a pin.
        2 : Enter (2) to deposit.
        3 : Enter (3) to withdraw.
        4 : Enter (4) to check balance.
        5 : Enter (5) to exit.
        Enter your choice: ''')
            
            if option == "1":
                self.create_pin()
            elif option == "2":
                self.deposit()
            elif option == "3":
                self.withdrawal()
            elif option == "4":
                self.balance_check()
            elif option == "5":
                self.exit()
                break  # Exit the loop
            else:
                print("Invalid option, please try again.")
    
    def create_pin(self):
        self.pin = input("Enter a new PIN: ")
        print(f"Your PIN {self.pin} has been set successfully!") 
    
    def check_pin(self):
        pin = input('Enter your PIN: ')
        if pin == self.pin:
            return True
        else:
            print("Invalid PIN. Please try again.")
            return False
  
    def deposit(self):
        if self.check_pin():
            amount = int(input("Enter the deposit amount: "))
            self.balance += amount
            print(f"You deposited {amount}. Your new balance is {self.balance}")
    
    def withdrawal(self):
        if self.check_pin():
            amount = int(input("Enter the withdrawal amount: "))
            if self.balance >= amount:
                self.balance -= amount
                print(f"You withdrew {amount}. Your new balance is {self.balance}")
            else:
                print("Insufficient balance.")
    
    def balance_check(self):
        if self.check_pin():
            print(f"Your current balance is {self.balance}")
    
    def exit(self):
        print("Thank you for using our ATM. Have a nice day!")

# Instantiate the ATM
sbi = Atm()
