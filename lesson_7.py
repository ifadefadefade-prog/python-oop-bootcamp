class Point:
    MAX_CORD = 100
    MIN_CORD = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_coord(self, x, y):
        if self.MINCORD <= x and y <= self.MAX_CORD:
            self.x = x
            self.y = y
    @classmethod
    def set_bound(cls, left):
        cls.MIN_CORD = left
    
    def __getattribute__(self, name):
        if name == 'x':
            raise ValueError('Доступ закрыт')
        else:
            print("__getattribute__")
            return object.__getattribute__(self, name)
    
    def __setattr__(self, name, value):
        if name == 'z':
            raise AttributeError('ОШИБКА')
        print('__setattr__')
        object.__setattr__(self, name, value)
        
    def __getattr__(self, name):
        return False
    
    def __delattr__(self, name):
        print(f'__delattr__:{name}')
        object.__delattr__(self, name)

pt = Point(2, 6)
pt2 = Point(23, 57)
print(pt.__dict__)
del pt.x
print(pt.__dict__)
