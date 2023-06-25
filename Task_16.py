# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# 1

list_1 = [1, 2, 2, 2, 2]
n = 2
count = 0
for i in range(len(list_1)):
    if n == list_1[i]:
        count += 1
print(count)