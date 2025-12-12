class Clock:
    __DAY = 86400
    
    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Seconds должны быть int')
        self.seconds = seconds % self.__DAY
    
    
    @classmethod
    def __verify_other(cls, other):
        if not isinstance(other, (int, cls)):
            raise ArithmeticError(f'')
        return other if isinstance(other, int) else other.seconds
        
    def __eq__(self, other):
        return self.seconds == self.__verify_other(other)
    
    def __lt__(self, other):
        return self.seconds < self.__verify_other(other) 
    
    
    
t1 = Clock(1000)
t2 = Clock(1000)
print(t1 < t2)