""""Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой."""
def new_function(**kwargs):
    print(' '.join(str(i) for i in kwargs.values()))


new_function(name='Иван', surname='Смирнов', birth_year='1993', city='СПБ', email='ivsm@mail.ru', tel='300-30-33')
