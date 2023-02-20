from OOPSample.Transport import Transport


class Auto(Transport):
    # вызываю родительский конструктор
    def __init__(self, name: str, wheels_count: int, season: str, is_need_to_permission: bool):
        super().__init__(name, wheels_count, season, is_need_to_permission)

    #переопределяю метод ride родителя Transport, также пишу две реализации -
    # автомобиль может ехать к конкретным координатам - например на карте
    # также он может ехать к точке назначения, которая задаётся названием места - строкой
    # таким образом я переопределил метод родителя и реализовал перегрузку методов одновременно
    def ride(self, destination: int):
        print("Место назначения выбрано по координатам: " f"{destination}")


    def ride(self, destination: str):
        print("Ваше место назначения: " f"{destination}")

