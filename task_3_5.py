"""Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу."""
# Вариант №1
def my_func():
    total = 0
    a = False
    while not a:
        user_num = input('Введите строку чисел, разделенных пробелом. Для завершения введите q: ').split()
        result = 0
        for i in range(len(user_num)):
            if user_num[i] == 'q':
                a = True
                break
            else:
                result += int(user_num[i])
        total += result
        print(total)


my_func()

# Вариант №2
def my_sum(my_list):
    items_sum = 0
    for item in my_list:
        try:
            items_sum += float(item)
        except ValueError:
            continue
    return items_sum


def sum_my_string(s):
    s = s.replace('#', '')
    s = s.replace(',', '.')
    numbers = s.split(' ')
    return my_sum(numbers)


numbers_sum = 0

while True:
    numbers_sting = input("Введите строку чисел, разделенных пробелом. Для завершения введите символ '#'\n")
    numbers_sum += sum_my_string(numbers_sting)
    if numbers_sum != 0:
        print(f"Сумма значений элементов {numbers_sum}")
    if numbers_sting.count('#') > 0:
        break
