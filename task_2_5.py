new_list = [7, 5, 3, 3, 2]
while True:
    n = input("Введите число от 1 до 10 или нажмите 'q' для выхода: ")
    if n != 'q':
        new_list.append(int(n))
        new_list.sort(reverse=True)
        print(new_list)
    else:
        break
