class Employee:
    position = "employee"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def base_info(self):
        print(f"This is a {self.position}. Their name is {self.name}. Their salary is {self.salary}.")


class RegularEmployee(Employee):
    position = "regular employee"

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.dep = department
        self.team = None

    def assign_team(self, teamlead):
        self.team = teamlead
        teamlead.team_members.append(self.name)

    def assign_dep(self, dephead):
        if self.dep == dephead.dep:
            dephead.subordinates.append(self.name)
        else:
            print("This employee doesn't belong to this department.")

    def info(self):
        self.base_info()
        print(f"They work in the {self.dep} department and they are a part of {self.team.name}'s team.")
        print("___________________")


class Trainee(Employee):
    position = "trainee"

    def __init__(self, name, salary, time):
        super().__init__(name, salary)
        self.probation_length = time

    def info(self):
        self.base_info()
        print(f"They haven't been assigned to a team yet and their probation period is {self.probation_length}.")
        print("___________________")


class Teamlead(RegularEmployee):
    position = "teamlead"

    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)
        self.team_members = []

    def info(self):
        self.base_info()
        print(f"Their team consists of {', '.join(x for x in self.team_members)}.\n"
              f"They work in the {self.dep} department.")
        print("___________________")


class DepartmentHead(Employee):
    position = "department head"

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.dep = department
        self.subordinates = []

    def assign_ceo(self, ceo):
        ceo.subordinates.append(self.name)

    def info(self):
        self.base_info()
        print(f"They are the head of the {self.dep} department.\n"
              f"Their subordinates are {', '.join(x for x in self.subordinates)}.")
        print("___________________")


class CEO(Employee):
    position = "CEO"

    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.subordinates = []

    def info(self):
        self.base_info()
        print(f"Their direct subordinates are {', '.join(x for x in self.subordinates)}.")
        print("___________________")


e_1 = RegularEmployee("Jenna Ramsey", 30000, "sales")
e_2 = RegularEmployee("Shane Nash", 30000, "sales")
e_3 = RegularEmployee("Erica Schmidt", 30000, "sales")
e_4 = RegularEmployee("Zack Wilson", 30000, "sales")
tr = Trainee("Clark Ellis", 15000, "2 weeks")
tl = Teamlead("Karen Roman", 60000, "sales")
e_1.assign_team(tl)
e_2.assign_team(tl)
e_3.assign_team(tl)
e_4.assign_team(tl)
dh = DepartmentHead("Tim Johns", 200000, "sales")
e_1.assign_dep(dh)
e_2.assign_dep(dh)
e_3.assign_dep(dh)
e_4.assign_dep(dh)
tl.assign_dep(dh)
ceo = CEO("Jeff Bezos", 100000000000000000000)
dh.assign_ceo(ceo)

e_1.info()
e_2.info()
e_3.info()
e_4.info()
tr.info()
tl.info()
dh.info()
ceo.info()
