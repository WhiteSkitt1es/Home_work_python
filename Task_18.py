# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

list_1 = [1, 12, 6, 7, 8, 15]
k = 11
# 12
max = 0
mid = 0
min = 0
for i in range(len(list_1)):
    if k == list_1[i]:
        mid = list_1[i]
    elif k == list_1[i] + 1:
        max = list_1[i]
    elif k == list_1[i] - 1:
        min = list_1[i]
if mid == k:
    print(mid)
elif min > mid:
    print(min)
else:
    print(max)