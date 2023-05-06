class BankAccount:
    def __init__(self, name, number, password):
        self.owner_name = name
        self.account_number = number
        self.__balance = 0
        self.__password = password

    def get_balance(self, password):
        if self.__password == password:
            return self.__balance
        else:
            print("Your current password is incorrect.")

    def get_password(self, password):
        if self.__password == password:
            return self.__password
        else:
            print("Your current password is incorrect.")

    def set_password(self, password, new_password):
        if self.__password == password:
            self.__password = new_password
        else:
            print("Your current password is incorrect.")

    def set_balance(self, password, change):
        if self.__password == password:
            if self.__balance + change >= 0:
                self.__balance += change
            else:
                print("You don't have enough money in your account.")
        else:
            print("Your current password is incorrect.")
