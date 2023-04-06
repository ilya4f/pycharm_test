'''Создать класс TrafficLight (светофор).Определить у него один атрибут color (цвет) и метод running (запуск);
Атрибут реализовать как приватный; В рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный; Продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый)
— 2 секунды, третьего (зелёный) — на ваше усмотрение; Переключение между режимами должно осуществляться
только в указанном порядке (красный, жёлтый, зелёный); Проверить работу примера, создав экземпляр
и вызвав описанный метод. Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.'''

from itertools import cycle
from time import sleep


class TrafficLight:
    __color = cycle([
        {'signal': 'red', 'duration': 7},
        {'signal': 'yellow', 'duration': 2},
        {'signal': 'green', 'duration': 4},
        {'signal': 'yellow', 'duration': 2}
    ])

    def running(self):
        light = next(self.__color)
        print(f"Сигнал {light['signal']}, пауза {light['duration']} сек.")
        sleep(light['duration'])


traffic_light = TrafficLight()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
