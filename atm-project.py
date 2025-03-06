class Atm:

    # static variable
    __counter = 1
    def __init__(self):

        # instance variable
        self.__pin = ""
        self.__balance = 0
        self.sno = Atm.__counter
        Atm.__counter = Atm.__counter + 1
        # self.menu()
    
    @staticmethod
    def get_counter():
        return Atm.__counter
    
    @staticmethod
    def set_counter(new_counter):
        if isinstance(new_counter,int):
            Atm.__counter = new_counter
        else:
            print("invalid")

    def get_pin (self):
        return self.__pin
    
    def set_pin(self, new_pin):
        if isinstance(new_pin, str): 
            self.__pin = new_pin
            print("Pin updated")
        else:
            print("Invalid pin. PIN must be a string.")

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
                self.__balance_check()
            elif option == "5":
                self.exit()
                break  # Exit the loop
            else:
                print("Invalid option, please try again.")
    
    def create_pin(self):
        self.__pin = input("Enter a new PIN: ")
        print(f"Your PIN {self.__pin} has been set successfully!") 
    
    def check_pin(self):
        pin = input('Enter your PIN: ')
        if pin == self.__pin:
            return True
        else:
            print("Invalid PIN. Please try again.")
            return False
  
    def deposit(self):
        if self.check_pin():
            amount = int(input("Enter the deposit amount: "))
            self.__balance += amount
            print(f"You deposited {amount}. Your new balance is {self.__balance}")
    
    def withdrawal(self):
        if self.check_pin():
            amount = int(input("Enter the withdrawal amount: "))
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"You withdrew {amount}. Your new balance is {self.__balance}")
            else:
                print("Insufficient balance.")
    
    def balance_check(self):
        if self.check_pin():
            print(f"Your current balance is {self.__balance}")
    
    def exit(self):
        print("Thank you for using our ATM. Have a nice day!")

# Instantiate the ATM
sbi = Atm()
hdfc =Atm()

print(sbi.sno)
print(hdfc.sno)

# print(sbi.get_pin())
# new_pin = "283972"
# sbi.set_pin(new_pin)
# print(sbi.get_pin())





