my_list = input('Введите целые числа через пробел: ').split(' ')
i, j = 0, 1
while len(my_list) > j:
    my_list[i], my_list[j] = my_list[j], my_list[i]
    i += 2
    j += 2
print('Результат:', *my_list)
