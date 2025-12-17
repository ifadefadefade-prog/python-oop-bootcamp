class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndentationError('Неверный индекс')

    def __setitem__(self, key, value):
        if 0 > key and not isinstance(key, int):
            raise TypeError('Неверно указан индекс')
        elif key > len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Неверно указан индекс')
        del self.marks[key]


s1 = Student('Vasya', [3, 4, 6, 5])
print(s1.__dict__)
s1[10] = 4
print(s1.__dict__)
del s1[2]
print(s1.__dict__)
