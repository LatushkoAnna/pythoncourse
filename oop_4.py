class TicketBooth:
    tickets_sold = 0

    def __init__(self, loc):
        self.loc = loc
        self.tickets = []
        self.tickets_sold = 0

    def sell(self, person):
        if self.loc == person.loc:
            if person.find_ticket(booth=self):
                print(f"{person.name} found a ticket! It costs {person.find_ticket(self).price} RUB. {person.name} has {person.money} RUB.")
                ticket = person.find_ticket(booth=self)
                if person.money >= ticket.price:
                    person.money -= ticket.price
                    print(f"{person.name} has bought a ticket from {self.loc} to {ticket.destination} for {ticket.price} RUB.")
                    print(f"{person.name} now has {person.money} RUB left.")
                    self.tickets_sold += 1
                    TicketBooth.tickets_sold += 1
                    person.loc = ticket.destination
                    print("\n_______________\n")
                else:
                    print(f"{person.name} doesn't have enough money to buy this ticket :(")
                    print("\n_______________\n")
            else:
                print(f"There's no ticket for {person.name} :(")
                print("\n_______________\n")
        else:
            print(f"{person.name} is not near this booth.")
            print("\n_______________\n")


class Person:
    trips_made = 0

    def __init__(self, name, loc, destination, money):
        self.name = name
        self.loc = loc
        self.destination = destination
        self.money = money

    def find_ticket(self, booth):
        for ticket in booth.tickets:
            if self.destination != ticket.destination:
                pass
            else:
                return ticket


class Ticket:
    def __init__(self, booth, destination, price):
        self.departure = booth.loc
        booth.tickets.append(self)
        self.destination = destination
        self.price = price


booth_1 = TicketBooth("Обское море")
ticket_1 = Ticket(booth_1, "Матвеевка", 30)
ticket_2 = Ticket(booth_1, "Сеятель", 30)
ticket_3 = Ticket(booth_1, "Речной вокзал", 40)
ticket_4 = Ticket(booth_1, "Новосибирск-Главный", 60)

booth_2 = TicketBooth("Новосибирск-Главный")
ticket_5 = Ticket(booth_2, "Инская", 40)
ticket_6 = Ticket(booth_2, "Дорогино", 115)
ticket_7 = Ticket(booth_2, "Жеребцово", 76)

person_1 = Person("Anya", "Обское море", "Новосибирск-Главный", 137)

booth_1.sell(person_1)
booth_1.sell(person_1)

person_1.destination = "Дорогино"

booth_2.sell(person_1)
