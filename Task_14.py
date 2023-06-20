# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n = int(input('Введите число: '))

count = 0
while count <= n:
    number = 2 ** count
    if number < n:
        print(number)
    count += 1