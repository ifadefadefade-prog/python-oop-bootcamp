from string import ascii_letters

class Person:
    
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()
    
    
    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        
        self.__fio = fio.split()
        self.old = old
        self.passport = ps
        self.weight = weight
        
    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError(f'ФИО - строка')
        f = fio.split()
        if len(f) != 3:
            raise TypeError(f"Неверный формат ФИО")
        
        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        
        for s in f:
            if len(s) < 1:
                raise TypeError('В ФИО ДОЛЖЕН БЫТЬ СИМВОЛ')
            
            if len(s.strip(letters)) != 0:
                raise TypeError('В ФИО НЕДОПУСТИМЫЕ СИМВОЛЫ')
            
    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError(f"Возарст должен быть целочисленным числом")
    
    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError(f"Вес должен быть вещественным числом")
    
    @classmethod
    def verify_ps(self, ps):
        if type(ps) != str:
            raise TypeError(f'ФИО - строка')
        temp = ps.split()
        if len(temp) != 2 or len(temp[0])!=4 or len(temp[1]) != 6:
            raise TypeError(f"Неверный формат паспорта")

        for p in temp:
            if not p.isdigit():
                raise TypeError(f'ДАННЫЕ ДЛЯ ПАСПОРТА ДОЛЖНЫ БЫТЬ ЧИСАЛМИ')
        
        
    @property
    def fio(self):
        return self.__fio
    @fio.setter
    def fio(self, fio):
        self.fio = fio
        
    @property
    def old(self):
        return self.__old
    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old
        
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight
        
    @property
    def ps(self):
        return self.__passport
    @ps.setter
    def ps(self, ps):
        self.verify_ps(ps)
        self.__passport = ps
        
        
new_pers = Person('Иванов Гнида Шлюха', 19, '3515 614413', 92.1)  
print(new_pers.__dict__)
new_pers.old = 48
new_pers.ps = '1234 842947'
new_pers.weight = 56.2
print(new_pers.__dict__)