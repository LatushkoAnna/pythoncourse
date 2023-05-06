class Bag:
    def __init__(self, color, number_key):
        self.color = color
        self._contents = []
        self.__number_key = number_key

    def get_number_key(self):
        return self.__number_key

    def get_contents(self):
        print(','.join(item for item in self._contents))


my_bag = Bag('pink', 116)
print(my_bag.color)
print(my_bag._contents)
my_bag.get_contents()
my_bag.get_number_key()
print(my_bag.__number_key)
