class Point:
    __slots__ = ('x', 'y', '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x**2 + y**2) ** 0.5

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


temp = Point(2, 4)
print(temp.length)
temp.length = 581
print(temp.length)
