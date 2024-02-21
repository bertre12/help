import requests
from rich import print as rprint
import json

# from pprint import pprint

"""
Requests - это модуль, который вы можете использовать для отправки всех видов HTTP-запросов. 
Это простая в использовании библиотека с множеством функций, начиная от передачи параметров 
в URL-адресах до отправки пользовательских заголовков и проверки SSL.

GET - метод используется для получения данных с сервера.
POST - метод используется для отправки данных на сервер.
OPTIONS - метод для "опроса" сервера о том, какие методы поддерживает ресурс. Поддерживается 
        не всеми сайтами/ресурсами.
PUT - метод для полного изменения/обновления данных.
PATCH - метод для частичного изменения/обновления данных.
DELETE - метод для удаления ресурса.

headers - Заголовок ответов.
elapsed - Время ответа.
is_redirect - Корректность ответа.
status_code - Статус запроса.
url - Окончательный URL-адрес ответа.
text - Отображение в str.
content - Если нетекстовый ответ.
json - Если есть JSON представление.
ok - Проверка на успешность запроса.
history - Показывает историю перенаправлений.
request - Показывает объект запроса.
reason - показывает текстовое представление ответа.
"""


"""Метод GET"""


# url = 'http://httpbin.org/get'  # Абстрактная переменная.
# response = requests.get(url, stream=True)  # Переменная.
#
# # Отображение GET запроса в виде словаря.

# rprint(response.headers)
# rprint(response.request.headers)
# rprint(response.headers['date'])  # По выбранному ключу. Не чувствителен к регистру.
#
# # Отображение GET запроса в виде JSON.
#
# rprint(response.json())
# rprint(response.json()['headers']['User-Agent'])  # По выбранному ключу. Чувствителен к регистру.
#
# # Запись полученного ответа JSON в файл.
#
# with open('name_file.json', 'w', encoding='utf-8') as f:  # Записать строку в файл.
#     json.dump(response.json(), f, indent=2)


"""Метод POST"""


# url = 'http://httpbin.org/post'  # Абстрактная переменная.
# payload = {'user_name': 'admin', 'password': 'password'}  # То, что хотим отправить.
#
# response = requests.post(url, stream=True, data=payload)
#
# rprint(response.text)


"""Метод OPTIONS"""


# url = 'http://httpbin.org'
# response = requests.options(url)
#
# rprint(response.headers)


"""Скачивание файлов"""


# 1 - Для файлов малого размера.

# url = 'https://www.python.org/static/img/python-logo.png'
# response = requests.get(url)
#
# with open('python_logo.png', 'wb') as image:
#     image.write(response.content)


# 2 - Для файлов неизвестного размера.

# url = 'https://www.python.org/static/img/python-logo@2x.png'
# response = requests.get(url, stream=True)
#
# with open('python_logo.png', 'wb') as image:
#     for chunk in response.iter_content(chunk_size=1024):
#         image.write(chunk)

# Как узнать размер файла.

# url = 'https://www.python.org/static/img/python-logo@2x.png'
# head_response = requests.head(url)
# image_size = int(head_response.headers['Content-Length'])
#
# rprint(f'Размер загружаемого файла: {image_size / 1024} кб')


"""Авторизация на сайте"""


# # 1 - Простой способ.
#
# url = 'https://httpbin.org/basic-auth/foo/bar'
# response = requests.get(url)  # Запрос на проверку на: пользователь авторизовался. Ошибка 401.
#
# rprint(response.status_code)
#
# response = requests.get(url, auth=('foo', 'bar'))  # Запрос на проверку на: пользователь авторизовался. С указанным
# # именем и паролем.
#
# rprint(response.status_code)
# rprint(response.request.headers['Authorization'])


# # 2 - Более сложный.
#
# url = 'https://httpbin.org/bearer'  # Вместо Bearer может быть Token или что-то другое.
# response = requests.get(url)  # Запрос на проверку на: пользователь авторизовался. Ошибка 401.
#
# rprint(response.status_code)
#
# headers = {'Authorization': 'Bearer some_token'}  # Переменная с ключом.
# response = requests.get(url, headers=headers)  # Запрос на проверку на: пользователь авторизовался. С указанием ключа.
#
# rprint(response.status_code)
