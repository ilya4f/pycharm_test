goods = []
analytics = {'name': [],
             'price': [],
             'quantity': [],
             'unit': []}
num = 1
while True:
    name = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    quantity = int(input('Введите количество товара: '))
    unit = input('Введите единицу измерения товара: ')
    params = {
        'name': name,
        'price': price,
        'quantity': quantity,
        'unit': unit
    }
    good = (num, params)
    goods.append(good)

    for key, value in params.items():
        i = analytics.get(key)
        if value in i:
            continue
        i.append(value)
        continue

    num += 1
    exit_answer = input('Ввести еще позицию? ').lower()
    if exit_answer == 'нет':
        break
print(analytics)
