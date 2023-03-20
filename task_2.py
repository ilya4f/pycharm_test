my_list = list(input('Введите целые числа через пробел:').split())
new_list = []
for i in range(0, len(my_list), 2):
    next_i = i + 2
    a = my_list[i:next_i]
    a.reverse()
    new_list.extend(a)
print(new_list)
