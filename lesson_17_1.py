class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__')
        return self.x ** 2 + self.y ** 2

    def __bool__(self):
        print('__bool__')
        return self.x == self.y


temp = Point(10, 10)
print(bool(temp))
if temp:
    print('Объект p - True')
else:
    print('Объект p - False')
