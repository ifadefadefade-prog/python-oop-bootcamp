class Vector:
    MIN_COORD = 0
    MAX_COORD = 100
    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD
    
    @staticmethod
    def norm2(x, y):
        return x*x + y*y
    
    def __init__(self, x=0, y=0):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        print(self.norm2(self.x,self.y))
    def get_coord(self):
        return self.x, self.y 
    
v = Vector(5, 2)
print(Vector.validate(5))
res = v.get_coord()
print(res)
print(Vector.norm2(5,6))