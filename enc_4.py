import re


class Smartphone:
    def __init__(self, number):
        self.__phone_number = number
        self.__contacts = []
        self.__apps = []

    def get_number(self):
        return self.__phone_number

    def get_contacts(self):
        return self.__contacts

    def get_apps(self):
        return self.__apps

    def set_number(self, new_number):
        if re.compile(r'^\+7\d{10}$').match(new_number):
            self.__phone_number = new_number
        else:
            print("This is not a valid number")

    def add_contact(self, contact):
        if re.compile(r'^\+7\d{10}$').match(contact):
            if contact not in self.__contacts:
                self.__contacts.append(contact)
            else:
                print("You already have this person's number.")
        else:
            print("This is not a valid number.")

    def install_app(self, app):
        if app not in self.__apps:
            self.__apps.append(app)
        else:
            print("You already have this app installed.")
