# Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# *Пример*

# 7, 2, 5 => 7, 9, 11, 13, 15

a = int(input("Введите первый элемент АП: "))
b = int(input("Введите разность элементов АП: "))
c = int(input("Введите колличество элементов АП: "))
list_1 = []
for i in range(c):
    if i <= c:
        i += 1
        ac = a + (i - 1) * b
        list_1.append(ac)
print(list_1)