import csv


class Product:
    def __init__(self, article_number: int):
        self.article_number = article_number

    def __repr__(self):
        print(f"{self.article_number}")

    @staticmethod
    def total_amount(count, price):
        return count * price


class Motorcycle(Product):
    it = 0

    def __init__(self, article_number: int, name: str, count: int, price: int, values=None):
        super().__init__(article_number)
        if values is None:
            values = []
        self.name = name
        self.count = count
        self.price = price
        self.values = [article_number, self.name, self.count, self.price]

    def generator(self):
        self.it = 0

        while self.it < len(self.values):
            yield self.values[self.it]
            self.it += 1

    def __repr__(self):
        return f"Motorcycle: ({self.article_number}, {self.name}, {self.count}, {self.price})"

    def __str__(self):
        return f"article_number {self.article_number}, name {self.name}, count {self.count}, price {self.price}"

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.values[item]


# class Equipment(Product):
#
#     def __init__(self, article_number: int, name: str, count: int, price: int, values=None):
#         super().__init__(article_number)
#         if values is None:
#             values = []
#         self.name = name
#         self.count = count
#         self.price = price
#         self.values = [article_number, self.name, self.count, self.price]
#
#     def generator(self):
#         self.it = 0
#
#         while self.it < len(self.values):
#             yield self.values[self.it]
#             self.it += 1
#
#     def __repr__(self):
#         return f"Motorcycle: ({self.article_number}, {self.name}, {self.count}, {self.price})"
#
#     def __str__(self):
#         return f"article_number {self.article_number}, name {self.name}, count {self.count}, price {self.price}"
#
#     def __setattr__(self, key, value):
#         self.__dict__[key] = value
#
#     def __getitem__(self, item):
#         return self.values[item]


def write_file_sort(read_filename, write_filename, param):
    # открываю файл благодаря with open -
    # после окончания работы с файлом он автоматом закроется
    data = []
    with open(read_filename) as file:
        # создаю экземпляр ридера, чтобы читать файл далее
        reader = csv.DictReader(file)
        with open(write_filename, "w", newline="") as file:
            # создаю экземпляр райтера - чтобы записывать в файл далее
            writer = csv.writer(file)
            for i in reader:
                data.append(Motorcycle(i["article_number"], i["name"], i["count"], i["price"]))
            print(data)
            sortedlist = sorted(data, key=lambda x: x[param], reverse=False)
            for i in sortedlist:
                writer.writerow(i)


def request_user():
    print(
        "Введите параметр, по которому нужно произвести сортировку: \n0 - article_number, 1 - name, 2 - count, 3 - price"
    )
    param = int(input())
    write_file_sort("data.csv", "new_data.csv", param)
    print("Готово! Проверьте файл new_data.csv!")


request_user()
