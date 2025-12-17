#    class Point:
#    MAX_COORD = 100
#    MIN_COORD = 0

def create_class_point(name: str, base: list, attrs: dict):
    attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
    return type(name, base, attrs)


class Point(metaclass=create_class_point):
    def get_coords(self):
        return (0, 0)


a = Point()
print(a.MAX_COORD)
print(a.get_coords())
