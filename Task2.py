# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

list = []
fact = 1

print("Введите N")
N = int(input())

for i in range(N):
    fact = fact * (i + 1)
    list.append(0)
    list[i] = fact

print(list)