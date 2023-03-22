new_list = input('Введите слова через пробел:').split()
for i, el in enumerate(new_list, 1):
    print(i, el[0:10])
