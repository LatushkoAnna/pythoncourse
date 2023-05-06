class Figure:
    def __init__(self):
        self.color = 'white'

    def change_color(self, color):
        self.color = color

    def print_info(self):
        pass


class Oval(Figure):
    name = "овал"

    def __init__(self, rx, ry):
        super().__init__()
        self.rx = rx
        self.ry = ry

    def print_info(self):
        print(f"Это {self.name}. Его цвет – {self.color}. Радиус 1 – {self.rx}. Радиус 2 – {self.ry}.")


class Square(Figure):
    name = "квадрат"

    def __init__(self, a):
        super().__init__()
        self.a = a

    def print_info(self):
        print(f"Это {self.name}. Его цвет – {self.color}. Длина его стороны – {self.a}.")


f_1 = Square(4)
f_1.change_color("green")
f_1.print_info()

f_2 = Oval(3, 7)
f_2.print_info()
