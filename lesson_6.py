from accessify import private, protected

class Point():
    def __init__(self, x=0, y=0):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
            
    #@private        
    @classmethod    
    def __check_value(cls, x):
        return type(x) in (int, float)
        
    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")
        
    def get_coord(self):
        return self.__x, self.__y
    
temp = Point('123', 24)
temp.set_coord(2, 6)
print(temp._Point__check_value(2))