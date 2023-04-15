class Box:
    def __init__(self, id):
        self.id = id
        self.shapes = []

    def put_in(self, shape):
        self.shapes.append(shape)

    def desc(self):
        print(f"Right now in the box #{self.id} there are:")
        for shape in self.shapes:
            shape.desc()


class Shape:
    name = None

    def __init__(self, id, color):
        self.id = id
        self.color = color
        self.box = None

    def desc(self):
        print(f"A {self.color} {self.name} with an ID={self.id}.")


class Square(Shape):
    name = "square"

    def __init__(self, id, color, side_length):
        self.a = side_length
        super().__init__(id, color)


class Circle(Shape):
    name = "circle"

    def __init__(self, id, color, radius):
        self.r = radius
        super().__init__(id, color)


class Triangle(Shape):
    name = "triangle"

    def __init__(self, id, color, a, b, cos):
        self.a = a
        self.b = b
        self.cos = cos
        super().__init__(id, color)


box_1 = Box(1)
shape_1 = Triangle(1, "blue", 15, 2, 30)
shape_2 = Circle(2, "pink", 3)
shape_3 = Square(3, "green", 5)

box_1.put_in(shape_1)
box_1.put_in(shape_2)
box_1.put_in(shape_3)
box_1.desc()
