# def function_name(x):
# body line 1
# ...
# body line n
# optional return

import modul as m  # замена имени модуля
from modul import *  # импорт всех функций
from modul import f
import modul


def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return (summa)


n = int(input())  # 5
print(sumNumbers(n))  # 15


def new_string(symbol, count):
    return symbol * count  # перемножение символа на число


print(new_string('!', 5))  # !!!!!
# print(new_string('!')) # TypeError missing 1 required ...


def concatenatio(*params):
    res = ""
    for item in params:
        res += item
    return res


print(concatenatio('a', 's', 'd', 'w'))  # asdw
print(concatenatio('a', '1'))  # a1
# print(concatenatio(1, 2, 3, 4)) # TypeError: ...

# -------------модули


print(modul.f(1))  # Целое
print(modul.f(2.3))  # 23
print(modul.f(28))  # None


print(f(1))


print(m.f(1))


# -----------------------рекурсия


def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)


list_1 = []

for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)  # [1, 1, 2, 3, 5, 8, 13, 21, 34]

# -------------------быстрая сортировка


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]

        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3, 7, 8, 9, 12, 56, 90]))

# ---------------------сортировка слиянием


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


nums = [38, 27, 43, 3, 9, 82, 10]
merge_sort(nums)
print(nums)
