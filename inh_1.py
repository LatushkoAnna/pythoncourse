class Table:
    def __init__(self, l, w, h):
        self.long = l
        self.width = w
        self.height = h

    def outing(self):
        print(self.long, self.width, self.height)


class Kitchen(Table):
    def howplaces(self, n):
        if n < 2:
            print("It is not kitchen table")
        else:
            self.places = n

    def outplases(self):
        print(self.places)


class Worker(Table):
    def __init__(self, l, w, h):
        super().__init__(l, w, h)
        self.is_busy = False
        self.places = 1

    def start_work(self):
        if not self.is_busy:
            self.is_busy = True
            print("You've started working")
        else:
            print("Sorry, but this table is already occupied :c")

    def finish_work(self):
        if self.is_busy:
            self.is_busy = False
            print("Good job today!")
        else:
            print("You're not even working right now!")


t_room1 = Kitchen(2, 1, 0.5)
t_room1.outing()
t_room1.howplaces(5)
t_room1.outplases()
t_2 = Worker(1, 3, 0.7)
t_2.outing()
t_2.start_work()
t_2.start_work()
t_2.finish_work()
