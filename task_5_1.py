'''Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.'''

input_not_empty = True
file = open('task_5_1.tmp.data', 'w', encoding='UTF-8')
while input_not_empty:
    line = input()
    if line == '':
        input_not_empty = False
    else:
        file.write(line + '\n')
file.close()
