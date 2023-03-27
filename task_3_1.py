"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""
# Вариант 1
def division(arg):
    try:
        dividend, divider = [int(_) for _ in arg]
        return f'{dividend / divider:.2f}'
    except ZeroDivisionError:
        print('Вы что? Пытаетесь делить на 0!')
    except ValueError:
        print('Некорректно введены значения')


print(division(input('Введите делимое число и делитель, через пробел: ').split()))

# Вариант 2
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return
    return result


try:
    n1 = float(input("a = "))
    n2 = float(input("b = "))
    print(f"a / b = {divide(n1, n2)}")
except ValueError:
    print("Incorrect input value")
