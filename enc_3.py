class Library:
    def __init__(self, name):
        self.__librarian = name
        self.__books = ['Book 1', 'Book 2', 'Book 3']

    def _is_librarian(self, name):
        return name == self.__librarian

    def add_book(self, name, book):
        if self._is_librarian(name):
            self.__books.append(book)
        else:
            print("You are not the librarian and cannot add books.")
