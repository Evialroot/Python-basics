"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

a = int(input("Введите целое положительное число: "))
max = a % 10
a = a // 10
while a > 0:
    if a % 10 > max:
        max = a % 10
    a = a // 10
print(max)
