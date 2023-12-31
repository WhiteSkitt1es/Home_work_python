# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

n = int(input('Введите количество монеток: '))

eagle = 0
tails = 0
while n > 0:
    coin = int(input('На монетке изображен орел (1) или решка (0)?'))
    if coin == 0:
        tails += 1
    else:
        eagle += 1
    n -= 1
if eagle > tails:
    print(f'Нужно перевернуть {tails} решки, чтобы все монетки лежали одной стороной.')
else:
    print(f'Нужно перевернуть {eagle} орлов, чтобы все монетки лежали одной стороной.')

