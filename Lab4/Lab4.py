class Product:
    def __init__(self, item_id: int):
        self.id = item_id

    def __repr__(self):
        print(f"{self.id}")


class Motorcycle(Product):
    values = []
    it = 0

    def __init__(self, article_number: int, name: str, count: int, price: int):
        super().__init__(article_number)
        self.name = name
        self.count = count
        self.price = price

    def generator(self):
        self.it = 0

        while self.it < len(self.values):
            yield self.values[self.it]
            self.it += 1

    def __repr__(self):
        return f"Motorcycle: ({self.id}, {self.name}, {self.count}, {self.price})"

    def __str__(self):
        return f"Артикул: {self.id},\n Название: {self.name},\n Количество: {self.count},\n Цена: {self.price}"

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.values[item]


class Equipment(Product):
    values = []
    it = 0

    def __init__(self, article_number: int, name: str, count: int, price: int):
        super().__init__(article_number)
        self.name = name
        self.count = count
        self.price = price

    def generator(self):
        self.it = 0

        while self.it < len(self.values):
            yield self.values[self.it]
            self.it += 1

    def __repr__(self):
        return f"Motorcycle: ({self.id}, {self.name}, {self.count}, {self.price})"

    def __str__(self):
        return f"Артикул: {self.id},\n Название: {self.name},\n Количество: {self.count},\n Цена: {self.price}"

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.values[item]

    @staticmethod
    def total_amount(count, price):
        return count * price


helmet = Equipment(1, "Just1 J18 Pulsar", 3, 22990)
triumph = Motorcycle(2, "Triumph Speed Twin", 1, 1_299_000)

print(helmet.__repr__())
print(helmet.__str__())
print(triumph.__repr__())
print(triumph.__str__())
