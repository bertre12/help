import csv
from rich import print as rprint

""" Запись без названия полей."""

# name_file = 'csv_1.csv'  # Переменная названия файла.

# dict_1 = {
#     'name': 'krunal',
#     'age': 26,
#     'education': 'Engineering'
# }  # Словарь для примера.
#
#
# with open(name_file, 'w', newline='', encoding='utf-8') as f:
#     for key in dict_1.keys():
#         f.write("%s,%s\n" % (key, dict_1[key]))

"""Запись с названием полей."""

# csv_columns = ['Service', 'ShowName', 'Seasons']  # Для заголовка.
#
# dict_2 = [
#     {'Service': 'Netflix', 'ShowName': 'Stranger Things', 'Seasons': 3},
#     {'Service': 'Disney+', 'ShowName': 'The Mandalorian', 'Seasons': 1},
#     {'Service': 'Hulu', 'ShowName': 'Simpsons', 'Seasons': 31},
#     {'Service': 'Prime Video', 'ShowName': 'Fleabag', 'Seasons': 2},
#     {'Service': 'AppleTV+', 'ShowName': 'The Morning Show', 'Seasons': 1},
# ]
#
# list_1 = [
#     ['Netflix', 'Stranger Things', 3],
#     ['Disney+', 'The Mandalorian', 1],
#     ['Hulu', 'Simpsons', 31],
#     ['Prime Video', 'Fleabag', 2],
#     ['AppleTV+', 'The Morning Show', 1]
# ]

# # Запись через список.

# with open(name_file, 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f, delimiter=',')
#     writer.writerow(csv_columns)  # Если используется заголовок.
#     writer.writerows(list_1)  # Запись всего списка.
#     # writer.writerow([])  # Запись построчно через список.
#     # rprint(csv_columns)
#
#     # for row in list_1:  # Запись всего списка через перебор.
#     #     writer.writerow(row)
#     #     rprint(row)  # Для отображения в консоли.

# # Запись через словарь.

# with open(name_file, 'w', newline='', encoding='utf-8') as f:
#     writer = csv.DictWriter(f, delimiter=',', fieldnames=csv_columns)
#     writer.writeheader()
#     for row in dict_2:
#         writer.writerow(row)
#         # rprint(row)  # Для отображения в консоли.

"""Чтение файла"""

# # Отображение списком.

# with open('csv_file.csv', 'r', newline='', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     # headers = next(reader)
#     # print('Headers: ', headers)  # Если есть столбцы заголовка.
#     for row in reader:
#         rprint(row)
# #         # rprint(row[]) # по индексу списка.

# Отображение словарём.

# with open('csv_file.csv', 'r', newline='', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         rprint(row)
#         # print(row[''])  # По названию столбца.
