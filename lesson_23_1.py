class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print('Geom')
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
#        self._name = self.__name


class Line(Geom):
    def draw(self):
        print('Линия')


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        self.fill = fill

    def get_coords(self):
        return (self._x1, self._y1)


r = Rect(0, 2, 3, 4)
print(r.__dict__)
print(r.get_coords())
print(r.__dict__)
