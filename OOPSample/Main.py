from OOPSample.Auto import Auto
from OOPSample.Bike import Bike

# создаю экземпляр велосипеда
bike = Bike("Ordinary bike", 2, "summer", False)

# получаю тип велосипеда через геттер
bike_type: str = bike.get_bike_type()
# print(bike_type)

# задаю тип велосипеда - горный
bike.set_bike_type("Mountain bike")
# получаю тип велосипеда
# print(bike.get_bike_type())

# создаю экземпляр автомобиля
automobile = Auto("Range Rover SVA", 4, "All seasons", True)

#automobile.ride(10)
#automobile.ride(destination="Hinkalnaya")


def choose_destination():
    print("Выберите точку назначения: или числовые координаты, или название места")
    print("Что будем вводить? 1 - координаты, 2 - название")
    method = int(input())
    match method:
        case 1:
            print("Введите координаты:")
            return int(input())
        case 2:
            print("Введите название места:")
            return input()


def request_user():
    print("Спасибо за выбор нашего бота для каршеринга!\nВыберите транспортное средство, на котором собираетесь поехать:\n1 - Автомобиль, 2 - Велосипед")
    print("Велосипед можно оставить в любом месте, а при выборе автомобиля нужно указать место назначения, куда вы собираетесь ехать")
    transport = int(input())
    match transport:
        case 1:
            print("Вы выбрали автомобиль!")
            destination = choose_destination()
            auto = Auto("Range Rover SVA", 4, "All seasons", True)
            auto.ride(destination)
        case 2:
            print("Вы выбрали велосипед!")
            bike = Bike("Mountain", 2, "Summer", False)
            bike.ride()


request_user()
