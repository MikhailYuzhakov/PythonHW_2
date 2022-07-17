# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

from matplotlib.pyplot import flag

list_1 = []
mlt = 1
flag = True

print("Введите N")
N = int(input())

for i in range(N):
    list_1.append(0)
    list_1[i] = randint(-N, N)  # генерируем список длинной N из случайных элементов в диапазоне от -N до N

print("Сгенерированный массив: ")
print(list_1)

for i in range(N-1):  # перемешиваем массив
    ranel = randint(0, N-2-i)  # записываем в переменную случайно сгенерированный индекс элемента, исключая последний
    cap = list_1[ranel]  # меняем местами случайный элемент массива с последним
    list_1[ranel] = list_1[N-1-i]
    list_1[N-1-i] = cap

print("Случайно перемешанный массив: ")
print(list_1)

with open("position.txt", 'r') as file:
    a = file.read()  # читаем индексы из файла
    list_of_index = a.split()  # разбиваем по строкам
list_of_index = list(map(int, list_of_index))  # преобразуем все элементы массива в тип int

for i in list_of_index:
    if i <= len(list_1) - 1:  # если элемент с указанным в файле индеком существует
        mlt = mlt * list_1[i]  # перемножаем его с остальными
    else:
        if (flag): 
            print("Не все указанные позиции существуют в массиве.")
            flag = False

print("Произведение существующих элементов массива на указанных позициях: ")
print(mlt)
        
        

