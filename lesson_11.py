class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координата должна быть целым числом')
        
    def __set_name__(self, owner, name):
        self.name = '_' + name
        
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)

class Point3D:
    
    x = Integer()
    y = Integer()
    z = Integer()
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        
temp = Point3D(3, 6, 9)
print(temp.__dict__, temp.z)