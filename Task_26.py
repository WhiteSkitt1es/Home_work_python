# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243
# A = 2; B = 3 -> 8 

a = int(input('Введите число А: '))
b = int(input('Введите число B: '))


def recursionSum(a,b):
    if b == 1:
        return a
    else:
        return a * recursionSum(a,b - 1)
    
print(recursionSum(a,b))