class Geom:
    def get_pr(self):
        raise NotImplementedError(f'В {self.__class__} нужно ' +
                                  'переопределить метод get_pr()')


class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2*(self.w + self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4*self.a


class Triangle(Geom):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_pr(self):
        return self.x + self.y + self.z


geom = [Rectangle(1, 2), Rectangle(4, 6), Square(10),
        Square(31), Triangle(2, 3, 6), Triangle(1, 6, 8)]
for i in geom:
    print(i.get_pr())
