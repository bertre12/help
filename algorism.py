"""Алгоритм поиска."""


# def scan(array, target):
#     for i in range(len(array)):
#         if array[i] == target:
#             return i
#     return -1
#
#
# print(scan([1, 4, 3, 5, 7, 9], 5))


"""Алгоритм бинарного поиска."""

# def sort(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         center = (left + right) // 2  # Вычисление середины массива.
#
#         if target == arr[center]:  # Если элемент в середине массива равен искомому элементу.
#             return center
#         elif target > arr[center]:  # Если искомый элемент больше элемента в середине.
#             left = center + 1
#         else:  # Если искомый элемент меньше элемента в середине.
#             right = center - 1
#     return -1  # Элемент не найден..
#
#
# arr = [34, 67, 23, 78, 90]
# target = 20
#
# result = sort(arr, target)
#
# if result != -1:
#     print(f'Элемент {target} найден на позиции {result}.')
# else:
#     print('Элемент н найден.')


"""Алгоритм сортировки выбором(selection sort)."""

# def selection_sort(array):
#     count = 0
#     for i in range(len(array)):
#         min_index = i
#         for j in range(i + 1, len(array)):
#             if array[j] < array[min_index]:
#                 min_index = j
#                 count += 1
#         array[i], array[min_index] = array[min_index], array[i]
#     print(f'Количество проходов - {count}')
#     return array
#
#
# print(selection_sort([]))


"""Алгоритм сортировки вставками((insertion sort)."""

# def insertion_sort(array):
#     count = 0
#     for i in range(1, len(array)):
#         key = array[i]
#         j = i - 1
#         while j >= 0 and key < array[j]:
#             array[j + 1] = array[j]
#             j -= 1
#             count += 1
#         array[j + 1] = key
#     print(f'Количество проходов - {count}')
#     return array
#
#
# print(insertion_sort([-10, 2, 30, 0, 23, 56, 1]))


"""Алгоритм быстрой сортировки(quick sort)."""

# def quick_sort(array):
#
#     if len(array) <= 1:
#         return array
#     else:
#         pivor = array[0]
#         less = [x for x in array[1:] if x <= pivor]
#         greater = [x for x in array[1:] if x > pivor]
#
#     return quick_sort(less) + [pivor] + quick_sort(greater)
#
#
# print(quick_sort([1, 5, 32, -10, 0]))

"""Алгоритм сортировки пузырьком(bubble sort)."""


# def bubble_sort(array):
#     n = len(array)
#     count = 0
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if array[j] > array[j + 1]:
#                 count += 1
#                 array[j], array[j + 1] = array[j + 1], array[j]
#     print(f'Количество проходов - {count}')
#     return array
#
#
# print(bubble_sort([-10, 2, 30, 0, 23, 56, 1]))


"""Алгоритм сортировки слиянием."""

# def merge_two_list(left: int, right: int) -> None:
#     """Функция разделения одного массива/списка на 2 равных."""
#     joint_len = left + right
#     new_list = []
#     while 0 != (len(joint_len)):
#         new_list.append(joint_len.pop(joint_len.index(min(joint_len))))
#     return new_list
#
#
# def merge_sort(joint_len: int) -> None:
#     """Функция сортировки массивов/списков через рекурсию."""
#     if len(joint_len) == 1:
#         return joint_len
#     return merge_two_list(merge_sort(joint_len[0:len(joint_len) // 2]), merge_sort(joint_len[len(joint_len) // 2:]))
#
#
# mas = list(map(int, input().split()))
# print(*merge_sort(mas))
