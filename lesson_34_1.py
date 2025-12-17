class Point:
    MAX_COORD = 100
    MIN_COORD = 0

class B1: pass
class C1: pass

def method1(self):
    print(self.__dict__)


A = type('Point', (B1, C1), {'MAX_COORD': 100, 'MIN_COORD': 0,
                             'method1': lambda self: self.MAX_COORD})
pt = A()
print(pt.MAX_COORD)
print(pt.method1())
