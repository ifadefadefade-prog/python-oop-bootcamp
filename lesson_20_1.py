class Geom:
    name = 'Geom'

    def set_coordds(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print('Линия')


class Rect(Geom):

    def draw(self):
        print('Прямогугольник')


g = Geom()
g.set_coordds(1, 1, 2, 2)
line = Line()
line.set_coordds(3, 3, 4, 6)
print(line.__dict__, line.name)
print(g.__dict__, g.name)
