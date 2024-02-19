import json
from rich import print as rprint

"""Создание файла"""

# name_file = 'json_1.json'  # Переменная названия файла.
#
# data = {
#     "president": {
#         "website": "pythonist.com",
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgeusian"
#     }
# }
# # 1 - Запись через dump
#
# with open(name_file, 'w', encoding='utf-8') as f:  # Записать строку в файл.
#     json.dump(data, f, indent=2)
#
# 2 - Запись через dumps

# json_string = json.dumps(data,  indent=2)  # Формирование в строку JSON.
# # json_string = json.dumps(data, sort_keys=True, indent=2)  # Формирование в строку JSON с сортировкой.
#
# with open(name_file, 'w', encoding='utf-8') as f:  # Записать строку в файл.
#     f.write(json_string)
#
# # rprint(json_string)

"""Чтение файла"""

# data_file = 'json_file.json'  # Переменная названия файла.
# data_file_1 = 'json_file_1.json'  # Переменная названия файла.

# # Чтение через load
# # 1 - С названием.

# with open(data_file, 'r') as f:
#     data = json.load(f)
#     for p in data['people']:
#         rprint('Name: ' + p['firstName'])
#         rprint('number: ' + p['number'])
#         rprint('')
#
# # rprint(data)
#
# # 2 - Без названия.
#
# with open(data_file_1, 'r') as f:
#     data = json.load(f)
#     for p in data:
#         rprint('Name: ' + p['firstName'])
#         rprint('number: ' + p['number'])
#         rprint('')
#
# # rprint(data)

# # Чтение через loads

# with open(data_file_1, 'r') as f:
#     # d = f.read()
#     # data = json.loads(d)
#
#     data = json.loads(f.read())
#     for p in data:
#         rprint('Name: ' + p['firstName'])
#         rprint('number: ' + p['number'])
#         rprint('')
#
# rprint(data)

