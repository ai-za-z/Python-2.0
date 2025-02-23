class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.__balance = balance
    def deposit(self,ammount):
        self.__balance += ammount
    def debit(self,ammount):
        if ammount <= self.__balance:
            self.__balance -= ammount
        else:
            return "Insufficient funds"
    def display_information(self):
        print(f"Account balance : {self.__balance}")
        print(f"Account holder {self.account_holder}")

my_account = BankAccount("Aizaz",12345)
my_account.display_information()
my_account.deposit(1000)
my_account.display_information()
my_account.debit(1000)
my_account.display_information()