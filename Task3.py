# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

list = []
summa = 0

print("Введите N: ")
N = int(input())

for i in range(N - 1):
    list.append(0)
    list[i] = pow((1 + 1/(i + 1)), i + 1)
    summa = summa + list[i]

print("Список последовательности: ")
print(list)
print("Сумма элементов послдовательности: ")
print(summa)
