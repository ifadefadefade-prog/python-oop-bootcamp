class Goods:
    def __init__(self, name, weight, price):
        super().__init__(2)
        print('init MixinLong')
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


class MixinLong:
    ID = 0

    def __init__(self, temp):
        print(self.__class__)
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f'{self.id}: товар был продан в 00 часов')

    def print_info(self):
        print(f'from MixinLong{self.name}, {self.weight}, {self.price}')


class Laptop(Goods, MixinLong):
    def print_info(self):
        MixinLong.print_info(self)


laptop1 = Laptop('Macbook', 1.5, 3000)
MixinLong.print_info(laptop1)
laptop1.print_info()
