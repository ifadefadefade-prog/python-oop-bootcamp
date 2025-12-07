class Point:
    color = 'red'
    circle = 2
    
    def set_coords(self, x, y):
        self.x = x
        self.y = y
        print(f"x={self.x}, y={self.y} - {self}")
        
    def get_coords(self):
        return (self.x, self.y)

pt = Point()
pt.set_coords(1, 2)
pt.get_coords() 

temp = Point()
temp.set_coords(2, 3)
print(temp.get_coords())
f = getattr(temp, 'get_coords')
print(f())
a = getattr(temp, 'set_coords')
print(a)