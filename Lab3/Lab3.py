import csv
import operator

motorcycles_data = [
    ("article_number", "name", "count", "price"),
    [1, "Triumph Speed Twin", 2, 1_299_990],
    [2, "Triumph Street Twin", 4, 990000],
    [3, "Triumph Truxton R", 3, 1_399_990],
    [4, "Triumph Bonneville T100", 5, 1_199_990],
]


def write_file_sort_str(read_filename, write_filename, param, method):
    with open(read_filename) as file:
        reader = csv.DictReader(file)
        with open(write_filename, "w", newline="") as file:
            header = ["article_number", "name", "count", "price"]
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            match method:
                case 1:
                    sortedlist = sorted(reader, key=lambda x: str(x[param]), reverse=False)
                case 2:
                    sortedlist = sorted(reader, key=lambda x: int(x[param]), reverse=False)
            for i in sortedlist:
                writer.writerow(i)
                print(i)


def request_user():
    print("Введите, как хотите отсортировать элементы файла: 1 - по строковому полю, 2 - по числовому")
    method = int(input())
    print("Введите параметр, по которому нужно произвести сортировку: \narticle_number, name, count, price")
    param = input()
    write_file_sort_str("data.csv", "new_data.csv", param, method)
    print("Готово! Проверьте файл new_data.csv!")


request_user()
