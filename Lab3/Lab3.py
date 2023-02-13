import csv
import os

motorcycles_data = [
    ("article_number", "name", "count", "price"),
    [1, "Triumph Speed Twin", 2, 1_299_990],
    [2, "Triumph Street Twin", 4, 990000],
    [3, "Triumph Truxton R", 3, 1_399_990],
    [4, "Triumph Bonneville T100", 5, 1_199_990],
]


def countFilesInDir(path):
    # os.walk - генерирует имена файлов в дереве каталогов,
    # она выдает тройной кортеж (dirpath, dirnames, filenames)
    print(f'Кол-во файлов в директории {path} = {sum(len(files) for _, _, files in os.walk(path))}')


def write_file_sort(read_filename, write_filename, param, method):
    # открываю файл благодаря with open -
    # после окончания работы с файлом он автоматом закроется
    with open(read_filename) as file:
        # создаю экземпляр ридера, чтобы читать файл далее
        reader = csv.DictReader(file)
        with open(write_filename, "w", newline="") as file:
            # т.к. использую DictWriter - нужно передать имена столбцов
            header = ["article_number", "name", "count", "price"]
            # создаю экземпляр райтера - чтобы записывать в файл далее, передаю файл и имена столбцов
            writer = csv.DictWriter(file, fieldnames=header)
            # записываю имена столбцов
            writer.writeheader()
            match method:
                case 1:
                    # сортирую список по строковому параметру
                    sortedlist = sorted(reader, key=lambda x: str(x[param]), reverse=False)
                case 2:
                    # сортирую список по числовому параметру
                    sortedlist = sorted(reader, key=lambda x: int(x[param]), reverse=False)
            for i in sortedlist:
                # записываю построчно результат в файл new_data.csv
                writer.writerow(i)
                print(i)


def request_user():
    print("Введите, как хотите отсортировать элементы файла: 1 - по строковому полю, 2 - по числовому")
    method = int(input())
    print("Введите параметр, по которому нужно произвести сортировку: \narticle_number, name, count, price")
    param = input()
    write_file_sort("data.csv", "new_data.csv", param, method)
    print("Готово! Проверьте файл new_data.csv!")


print(countFilesInDir("C:/Users/solda/Desktop/PythonLabs/Lab3"))
request_user()
