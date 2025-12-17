class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print('Geom')
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print('Линия')


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        print('rect')
        self.fill = fill

    def draw(self):
        print('rect')


line = Line(0, 2, 5, 1)
r = Rect(1, 4, 6, 1)
print(r.__dict__)
