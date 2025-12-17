from dataclasses import dataclass, field, InitVar


class Vector3D:
    def __init__(self, x: int, y: int, z: int, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.length = ((self.x**2 + self.y**2 + self.z**2) ** 0.5 if calc_len else 0)


@dataclass
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = (self.x**2 + self.y**2 + self.z**2) ** 0.5


v = V3D(2, 4, 6, True)
print(v)
