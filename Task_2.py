# Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# number = input('Введите число: ')
# if number >= 100:

number = input('Введите трехзначное число: ')

if len(number) == 3:
    sum = int(number[0]) + int(number[1]) + int(number[2])
    print(sum)
else:
    print('Ошибка, введите трехзначное число!')