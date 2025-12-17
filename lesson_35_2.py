class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
        return type.__new__(cls, name, base, attrs)

#    def __init__(cls, name, base, attrs):
#        super().__init__(name, base, attrs)
#        cls.MAX_COORD = 100
#        cls.MIN_COORD = 0


class Point(metaclass=Meta):
    def get_coords(self):
        return (0, 0)


a = Point()
print(a.MAX_COORD)
print(a.get_coords())
