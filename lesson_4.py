class Point():
    def __new__(cls, *args, **kwargs):
        print(f"Вызов __new__ для {str(__name__)}")
        return super().__new__(cls)
    
    def __init__(self, x=0, y=0, z=0):
        print(f"Вызов __init__ для {str(__name__)}")
        self.x = x
        self.y = y
        self.z = z
        
temp = Point(1, 2, 5)
print(temp.__dict__)