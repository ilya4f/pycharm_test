"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""
def division(arg):
    try:
        dividend, divider = [int(_) for _ in arg]
        return f'{dividend / divider:.2f}'
    except ZeroDivisionError:
        print('Вы что? Пытаетесь делить на 0!')
    except ValueError:
        print('Некорректное введение значений')


print(division(input('Введите делимое число и делитель, через пробел: ').split()))
