def f(x):
    return x ** 2
print(f(2))

print(type(f))

g = f

print(f(4)) # 16
print(g(4)) # 16


def calc1(x):
    return x + 10
print(calc1(10)) # 20

def calc2(x):
    return x * 10
print(calc2(10)) #100

def math(op, x):
    print(op(x))
    
math(calc2, 10) # 100

def sum(x, y):
    return x + y
def mylt(x, y):
    return x * y

def calc(op, a, b):
    print(op(a, b))
    
calc(mylt, 4, 5) # 20


f = sum
calc(f, 4, 5) # 9

#  sum = lambda x, y: x + y

calc(lambda x, y: x + y, 4, 5) # 9
calc(lambda x, y: x * y, 4, 5) # 20

# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить
# список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
out = []
for i in data :
    if i % 2 == 0:
        out.append((i, i ** 2))
print(out) # [(2, 4), (8, 64), (38, 1444)]

# при использовании lambda

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)

res = where(lambda x: x % 2 == 0, res)
print(res) # [2, 8, 38]


res = list(select(lambda x: (x, x ** 2), res))
print(res) # [(2, 4), (8, 64), (38, 1444)]

# функция map (итератор)

list_1 = [x for x in range (1,10)]
print(list_1)
list_1 = list(map(lambda x: x * 10, list_1 ))
print(list_1)

#  Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки. Как
# превратить list строк в list чисел?

data = '1 2 3 5 8 15 23 38'
print(list(data)) # ['1', ' ', '2', ' ', '3', ' ', '5', ' ', '8', ' ', '1', '5', ' ', '2', '3', ' ', '3', '8']

print(data.split()) # ['1', '2', '3', '5', '8', '15', '23', '38']

data = list(map(int,data.split()))
print(data) # [1, 2, 3, 5, 8, 15, 23, 38]
print()
#-----------------
def where(f, col):
    return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = where(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res) # [(2, 4), (8, 64), (38, 1444)]
print()
#  функция filter

data = '1 2 3 5 8 15 23 38'.split()
print(data)
res = list(map(int, data))
print(res)

res = list(filter(lambda x: x % 2 == 0, res))
print(res)

res = list(map(lambda x: (x, x ** 2), res))
print(res)

data = [x for x in range(10)]
res = list(filter(lambda x: x % 2 == 0, data))
print(res) # [0, 2, 4, 6, 8]


# функция zip

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# работает по минимальному входящему набору

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7, 9]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]

# функция enumerate

users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]

# файлы--------------------------------------------------------

# 1. a – открытие для добавления данных.
# o Позволяет дописывать что-то в имеющийся файл.
# ○ Если вы попробуете дописать что-то в несуществующий файл, то файл
# будет создан и в него начнётся запись.
# 2. r – открытие для чтения данных.
# ○ Позволяет читать данные из файла.
# ○ Если вы попробуете считать данные из файла, которого не существует,
# программа выдаст ошибку.
# 3. w – открытие для перезаписи данных.
# ○ Позволяет записывать данные и создавать файл, если его не
# существует.
# Миксованные режимы:
# 4. w+
# ○ Позволяет открывать файл для записи и читать из него.
# ○ Если файла не существует, он будет создан.
# 5. r+
# ○ Позволяет открывать файл для чтения и дописывать в него.
# ○ Если файла не существует, программа выдаст ошибку.

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать (a - открытие для добавления данных)
data.writelines(colors) # разделителей не будет
data.close()


with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
    
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors) # разделителей не будет
data.close()


# модуль OS

#● os.chdir(path) - смена текущей директории.
import os
os.chdir#('C:/Users/79190/PycharmProjects/GB')
#● os.getcwd() - текущая рабочая директория
import os
print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject'


# модуль shutil

# import shutil
# Познакомимся с базовыми функциями данного модуля:
# ● shutil.copyfile(src, dst) - копирует содержимое (но не метаданные) файла src в
# файл dst.
# ● shutil.copy(src, dst) - копирует содержимое файла src в файл или папку dst.
# ● shutil.rmtree(path) - Удаляет текущую директорию и все поддиректории; path
# должен указывать на директорию, а не на символическую ссылку.