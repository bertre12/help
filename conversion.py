import csv
import json

"""Конвертация JSON в CSV"""

# with open('json_file.json', 'r') as f:  # С названием в файле.
#     # data = json.load(f)
#     data = json.loads(f.read())
#     people = data["people"]
#
# with open('names_1.csv', 'w', newline='', encoding='utf-8') as f:
#     x = people[0].keys()
#     writer = csv.DictWriter(f, fieldnames=x)
#     writer.writeheader()
#     for i in people:
#         writer.writerow(i)


# with open('json_file_1.json', 'r') as f:  # Без названия в файле.
#     data = json.loads(f.read())
# x = ','.join(*[data[0]])  # Переменная.
# for i in data:
#     x += f'\n{i["firstName"]}, {i["lastName"]}, {i["gender"]}, {i["age"]}, {i["number"]}'
#
# with open('names_2.csv', 'w', newline='', encoding='utf-8') as f:
#     f.write(x)


"""Конвертация CSV в JSON"""

# with open('.csv', 'r', newline='', encoding='utf-8') as f:  # С названием в файле.
#     reader = csv.reader(f)
#     next(reader)  # Для удаления заголовка если он есть.
#     data = {"people": []}
#
#     for i in reader:
#         data["people"].append({"firstName": i[0], "lastName": i[1], "gender": i[2], "age": i[3], "number": i[4]})
#
# with open('.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, indent=2)
#
#
# with open('.csv', 'r', newline='', encoding='utf-8') as f:  # Без названия в файле.
#     reader = csv.reader(f)
#     next(reader)  # Для удаления заголовка если он есть.
#     data = []
#
#     for i in reader:
#         data.append({"firstName": i[0], "lastName": i[1], "gender": i[2], "age": i[3], "number": i[4]})
#
# with open('.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, indent=2)
