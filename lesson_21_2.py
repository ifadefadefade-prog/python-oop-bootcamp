class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))


v = Vector([1, 5, 3, 6, 7])
print(v)
