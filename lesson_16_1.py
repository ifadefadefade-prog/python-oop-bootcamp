class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self, other):
        return hash((self.x, self.y))


temp = Point(2, 4)
temp2 = Point(2, 4)
d = {}
d[temp] = 1
d[temp2] = 2
print(d)
