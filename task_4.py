n = int(input("Введите целое положительное число:"))
number_max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > number_max:
        number_max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе:", number_max)
        break
