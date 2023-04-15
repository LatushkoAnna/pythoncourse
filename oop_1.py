class Library:
    books_rented = 0

    def __init__(self, name, books):
        self.name = name
        self.books = books.split('; ')
        self.books_rented = 0

    def rent(self, person, book):
        self.books.remove(book)
        person.books.append(book)
        print(f"{person.name} rented \"{book}\" from \"{self.name}\".")
        print(f"{person.name} has these books: {person.books}.")
        print(f"These books are still in \"{self.name}\": {self.books}.")
        self.books_rented += 1
        print(f"{self.name} rented out {self.books_rented} books.")
        Library.books_rented += 1


class Person:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.books_rented = 0


person_1 = Person("Anya")
library_1 = Library("Научная библиотека НГУ", "Методы математической лингвистики в стилистических исследованиях; "
                                              "Методические указания к курсу \"Современный русский литературный "
                                              "язык\". (Раздел Фонетика); Метафоры, которыми мы живем; "
                                              "Толково-комбинаторный словарь русского языка: опыты "
                                              "семантико-синтаксического описания русской лексики")

library_1.rent(person_1, "Метафоры, которыми мы живем")
