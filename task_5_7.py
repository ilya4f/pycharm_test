'''Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать. Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.'''

import json

with open('task_5_7.data', 'w') as f:
    f.write('firm_1 ООО 12000 6000\n')
    f.write('firm_2 ООО 6000 10000\n')
    f.write('firm_3 ИП 7000 4000\n')
    f.write('firm_4 ЗАО 15000 10000\n')

profit_dict = {}
total_profit = 0
count_profit = 0
with open('task_5_7.data') as f:
    for line in f:
        name, form, income, expenses = line.split()
        income = int(income)
        expenses = int(expenses)
        profit = income - expenses
        if profit > 0:
            profit_dict[name] = profit
            total_profit += profit
            count_profit += 1
        else:
            profit_dict[name] = -expenses

if count_profit != 0:
    average_profit = total_profit / count_profit
    average_profit_dict = {"average_profit": average_profit}
else:
    average_profit_dict = {"average_profit": 0}

result_list = [profit_dict, average_profit_dict]
with open('task_5_7_data.json', 'w') as f:
    json.dump(result_list, f)
