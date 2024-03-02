import logging

"""
Logging- это модуль в стандартной библиотеке, который обеспечивает возможность работы со средой
для выпуска сообщений журнала из программ. Логирование используется для отслеживания событий,
происходящих при запуске программного обеспечения.
"""

"""Настройка уровня логирования, чтоб начиналось от указанного, а не по умолчанию от WARNING.

level - уровень логирования.
filename - запись данных в файл.
filemode - способ открытия файла. (w - режим перезаписи)
encoding - кодировка символов.
format - формат записи для каждой строки.
datefmt - формат записи даты.
"""

# logging.basicConfig(level=logging.DEBUG, filename='log.log', filemode='w', encoding='utf-8',
#                     format='%(asctime)s - %(levelname)s - %(message)s',
#                     datefmt='%d.%m.%y %H:%M:%S')
#
# logging.debug('debug')  # Отладочная информация.
# logging.info('info')  # Информация о ходе работы.
# logging.warning('warning')  # Предупреждение.
# logging.error('error')  # Ошибка.
# logging.critical('critical')  # Критическая ошибка.


"""Отслеживание трассировки стека и обработка исключений."""

"""
Трассировка стека  — это отчёт о действующих кадрах стека в определённый момент времени во время выполнения программы.
"""

# logging.basicConfig(level=logging.DEBUG, filemode='w', encoding='utf-8',
#                     format='%(asctime)s - %(levelname)s - %(message)s',
#                     datefmt='%d.%m.%y %H:%M:%S')
#
# num_1 = 25
# num_2 = 0
#
# # 1 Способ
#
# # try:
# #     value = num_1 / num_2
# # except ZeroDivisionError as e:
# #     logging.error('ZeroDivisionError', exc_info=True)
#
# # 2 Способ
#
# # try:
# #     value = num_1 / num_2
# # except ZeroDivisionError as e:
# #     logging.exception('Ошибка деления на 0')

# пользовательское тестирование.

"""Создание пользовательского логера."""


# logger = logging.getLogger('__name__')  # Создание объекта логирования.
# logger.setLevel(logging.DEBUG)  # Установка порога логирования.
#
# handler = logging.FileHandler('log_1.log', 'w', 'utf-8')  # Создание обработчика файлов для записи.
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                               datefmt='%d.%m.%y %H:%M:%S')  # Шаблон для отображения в журнале.
# handler.setFormatter(formatter)  # Связывание обработчика с шаблоном форматирования.
#
# logger.addHandler(handler)  # Добавление обработчиков логеру.
#
# logger.info('test logger')  # Использование логера.


"""Логирование в несколько мест."""


# logger = logging.getLogger('__name__')
# logger.setLevel(logging.DEBUG)
#
# file_handler = logging.FileHandler('log_1.log', 'w', 'utf-8')
# file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d.%m.%y %H:%M:%S'))
#
# # file_handler = logging.FileHandler('log_1.log', 'w', 'utf-8')
# # file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d.%m.%y %H:%M:%S')
# # file_handler.setFormatter(file_formatter)
#
# console_handler = logging.StreamHandler()  # Отображение в консоль.
# console_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
#
# logger.addHandler(file_handler)
# logger.addHandler(console_handler)
#
# logger.info('test logger')


"""Сторонняя библиотека для логирования."""

from loguru import logger


"""Создание объекта логирования и его частичная настройка."""


# logger.add('log.log', level='DEBUG', rotation='1 mb',
#            format='{time:DD.MM.YY - HH:mm:ss} - {level} - {file}:{line} - {message}')
#
#
# logger.debug('Это сообщение отладочного уровня')
# logger.info('Информационное сообщение')
# logger.warning('Предупреждение')
# logger.error('Сообщение об ошибке')
# logger.critical('Критическое сообщение')


"""Отслеживание трассировки стека и обработка исключений."""

# # 1 Способ
#
# def my_function():
#     try:
#         1 / 0
#     except Exception as e:
#         logger.exception("Error:")
#
#
# my_function()
#
# # 2 Способ
#
# logger.add("log.log", format="{time} {level} {message}")
#
#
# @logger.catch
# def my_function(x, y):
#     return x / y
#
#
# my_function(1, 0)

"""Логирование в несколько мест."""


# logger.add('log.log', level='DEBUG')
#
# logger.debug('debug_base')
# logger.info('info_base')
#
#
# logger.add('log.log', level='DEBUG',
#            format='{time:YYYY-MM-DD at HH:mm:ss} | {level} | {file}:{line} | {message}')
#
# logger.debug('debug_v1')
# logger.info('info_v1')