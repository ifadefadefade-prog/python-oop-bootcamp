class Point:
    color = 'red'
    circle = 2
    
    def __init__(self, x=1, y=2):
        self.x = x
        self.y = y
    
    def __del__(self):
        print(f"Экзепляр {str(__name__)} удален")
    
    def set_coords(self, x, y):
        self.x = x
        self.y = y
        print(f"x={self.x}, y={self.y} - {self}")
        
    def get_coords(self):
        return (self.x, self.y)

    
new_class = Point(2, 3)
print(new_class.__dict__)
new_class.set_coords(6, 20)