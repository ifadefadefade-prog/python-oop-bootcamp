from dataclasses import dataclass, field


class Thing:
    def __init__(self, name, weight, price, dims=[]):
        self.name = name
        self.weight = weight
        self.price = price
        self.dims = dims

    def __repr__(self):
        return f"Thing: {self.__dict__}"


@dataclass
class ThingData:
    name: str
    weight: int = 100
    price: float = 0
    dims: list = field(default_factory=list)


t1 = ThingData('Учебник по матанализу', 100, 1040)
print(t1)
t1.dims.append(10)
print(t1)
t2 = ThingData('Учебник по матанализу', 100, 1040)
print(t2)
