from OOPSample.Transport import Transport


class Bike(Transport):
    # вызываю родительский конструктор
    def __init__(self, name: str, wheels_count: int, season: str, is_need_to_permission: bool):
        super().__init__(name, wheels_count, season, is_need_to_permission)

    # переопределяю метод ride родителя Transport
    def ride(self):
        print("Bike is ride")

    # создаю приватное поле
    __bike_type = "Ordinary bike"

    # создаю геттер для поля bike_type
    def get_bike_type(self):
        return self.__bike_type

    # создаю сеттер для поля bike_type
    def set_bike_type(self, bike_type: str):
        self.__bike_type = bike_type
