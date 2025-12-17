from dataclasses import dataclass, field, InitVar
from typing import Any


class GoodsMethodsFactory:
    @staticmethod
    def get_init_measure():
        return [0, 0, 0]


@dataclass
class Goods:
    current_uid = 0
    uid: int = field(init=False)
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print('Goods: post_init')
        self.__class__.current_uid += 1
        self.uid = self.__class__.current_uid


@dataclass
class Book(Goods):
    title: str = ''
    author: str = ''
    price: float = 0
    weight: int | float = 100
    measure: list = field(default_factory=GoodsMethodsFactory.get_init_measure)

    def __post_init__(self):
        super().__post_init__()
        print('Book: post_init')


b1 = Book(1500, 300, 'Война и Мир', 'Толстой Л.Н.')
print(b1)
