class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point):
    __slots__ = 'z',

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


temp = Point3D(1, 4, 22)
del temp.x
temp.x = 94
print(temp.x)
temp.z = 74
print(temp.z)
print(temp.x)
