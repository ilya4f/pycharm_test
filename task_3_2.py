""""Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой."""
def new_function(**kwargs):
    print(' '.join(str(i) for i in kwargs.values()))


new_function(name='Иван', surname='Смирнов', birth_year='1993', city='СПБ', email='ivsm@mail.ru', phone='300-30-33')

# Вариант 2
def print_user(name, surname, birth_year, city, email, phone):
    print(f"Пользователь {name} {surname} {birth_year}-го года рождения, проживающий в городе {city}, "
          f"имеет  Email {email} и телефон {phone}")


user_template = {
    'name': 'Имя',
    'surname': 'Фамилия',
    'birth_year': 'Год рождения',
    'city': 'Город проживания',
    'email': 'Email',
    'phone': 'Телефон'
}
my_user = {}
for key, value in user_template.items():
    input_value = input(f'{value}: ')
    my_user.update({key: input_value})

print_user(**my_user)
