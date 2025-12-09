class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old
        
    @property
    def old(self):
        return self.__old
    
    @old.setter
    def old(self, old):
        self.__old = old
    
    @old.deleter
    def old(self):
        del self.__old
    
    def get_name(self):
        return self.__name
     
h1 = Person('Dima', 13)
del h1.old
print(h1.__dict__)