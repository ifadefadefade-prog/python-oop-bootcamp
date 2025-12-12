class Clock:
    __DAY = 86400
    
    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Seconds должны быть int')
        self.seconds = seconds % self.__DAY
        
        
    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (m // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"
    
    
    @classmethod
    def __get_formatted(cls, x):
        return str(x).ljust(2, '0')
    
    def __add__(self, other):
        if not isinstance(other, (int, self.__class__)):
            raise ArithmeticError("Првый операнд должен быть целым числом!")
        temp = other
        if isinstance(other, self.__class__):
            temp = other.seconds
        return self.__class__(self.seconds + temp)
    
    def __radd__(self, other):
        return self + other
    
    def __iadd__(self, other):
        if not isinstance(other, (int, self.__class__)):
            raise ArithmeticError('Seconds должны быть int')
        temp = other
        if isinstance(other, self.__class__):
            temp = other.seconds
        self.seconds += temp
        return self
        
temp = Clock(1000)
temp2 = Clock(2000)
temp3 = Clock(3000)
temp = 1000 + temp
print(temp.get_time())