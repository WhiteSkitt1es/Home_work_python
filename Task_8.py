# # Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# # если разрешается сделать один разлом по прямой между дольками
# # (то есть разломить шоколадку на два прямоугольника).
# # *Пример:*

# # 3 2 4 -> yes
# # 3 2 1 -> no

a = int(input('Введите длину шоколадки в дольках: '))
b = int(input('Введите ширину шоколадки в дольках: '))
c = int(input('Введите количество долек которые вы хотите отломить: '))
if c > a * b:
    print('Нельзя отломить больше долек чем сама шоколадка!')
elif c == a * b:
    print('Делить целую шоколадку не нужно.')
else:
    if c % a == 0 or c % b == 0:
        print('Шоколадку поделить можно!')
    else:
        print('Шоколадку поделить нельзя!')