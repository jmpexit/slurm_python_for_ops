#Создайте класс для агента сбора метрик. Эмулировать периодический сбор событий не нужно.
#Агент должен иметь IP адрес сервера к которому подключается, хранить ключ доступа к серверу
# и иметь возможность управлять периодом сбора метрик(в секундах) и периодом отправки событий на сервер сбора событий (в секундах).
# методы управления агентом:
#Собрать события: при его использовании должно выводиться сообщение "события сервера <IP-адрес> собраны. Следующий сбор через <период сбора метрик> секунд".
#Отправка событий на сервер сбора метрик: выводится сообщение "события сервера <IP-адрес> собраны отправлены на сервер сбора метрик.
#Следующиая отправка через <период отправки событий на сервер сбора событий> секунд".
#Обнуление кеша агента: выводится сообщение "кеш агента был очищен" и  число вызовов метода сборки событий сбрасывается на 0.
#Получение информации о числе собранных событий: выводится сообщение "С сервера <IP-адрес> собрано <число вызовов метода сборки событий> событий".


def count_calls(func):
    def wrapper(self):
        wrapper.calls += 1
        print(f'Функция {func.__name__} была вызвана {wrapper.calls} раз(а)')
        return func(self)
    wrapper.calls = 0
    return wrapper


class MetricsAgent(): # объявление класса
    """
    Агент сбора метрик
    """
    count = 0
    def __init__(self, dst_ip_addr: str, access_key: str, collect_period: int, send_period: int):
        """
        Конструктор
        :param dst_ip_addr: IP адрес сервера, к которому подключается агент
        :param access_key: ключ доступа к серверу
        :param collect_period: период сбора метрик (в секундах)
        :param send_period: период отправки событий на сервер сбора событий (в секундах)
        """
        self.__dst_ip_addr = dst_ip_addr
        self.__access_key = access_key
        self.__collect_period = collect_period
        self.__send_period = send_period

    def collect_events(self):
        """
        Сбор событий
        :return:
        """
        print(f'События сервера {self.__dst_ip_addr} собраны. Следующий сбор через {self.__collect_period} секунд')

    #@count_calls
    def send_events(self):
        """
        Отправка событий
        :return:
        """
        self.count += 1
        print(f'События сервера {self.__dst_ip_addr} собраны и отправлены на сервер сбора метрик. '
              f'Следующиая отправка через {self.__send_period} секунд;\n')
             # f'С сервера {self.__dst_ip_addr} собрано {count_calls(self)} событий')

    # TODO Получение информации о числе собранных событий: выводится сообщение "С сервера <IP-адрес> собрано <число вызовов метода сборки событий> событий".
    def events_count(self):
        """
        Получение информации о числе собранных событий
        :return:
        """
        #print(f'!!!Я - МЕТОД КЛАССА!!! С сервера {self.__dst_ip_addr} собрано {count_calls()} событий')
        #c = count_calls(self.send_events())
        print(self.count)

    #TODO Обнуление кеша агента: выводится сообщение "кеш агента был очищен" и  число вызовов метода сборки событий сбрасывается на 0.
    def clear_cache(self):
        """
        Очистка кэша событий
        :return:
        """
        self.count = 0
        print('кеш агента был очищен')


def main():
    agent = MetricsAgent(1, 1, 1, 2)
    agent.collect_events()
    agent.send_events()
    agent.send_events()
   # agent.count_calls()
    agent.events_count()
    agent.clear_cache()
    agent.events_count()
    agent.send_events()
    agent.events_count()

if __name__ == '__main__':
    main()


#ПРИМЕР
# def method_friendly_decorator(method_to_decorate):
#     def wrapper(self, lie):
#         lie = lie - 3  # действительно, дружелюбно - снизим возраст ещё сильней :-)
#         return method_to_decorate(self, lie)
#
#     return wrapper
#
#
# class Lucy(object):
#
#     def __init__(self):
#         self.age = 32
#
#     @method_friendly_decorator
#     def sayYourAge(self, lie):
#         print
#         "Мне %s, а ты бы сколько дал?" % (self.age + lie)
#
#
# l = Lucy()
# l.sayYourAge(-3)
# # выведет: Мне 26, а ты бы сколько дал?