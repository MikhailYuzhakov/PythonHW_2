# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

print("Введите число")
a = input()
summa = 0

for digit in a:
    if digit != '.':
        dig = int(digit)
        summa = summa + dig

print("Сумма цифр в числе: ",summa)