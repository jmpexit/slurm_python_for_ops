# при реконфигурации должна быть возможность задать период в формате "<Число>h<Число>m<Число>s",
# Порядок следования гарантировано не будет нарушен и других вариаций быть не может.
# Но какие-то части выражения могут отсутствовать. Например будут валидными значения:
# 1h32m14s
# 32m14s
# 1h14s
# 14s

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
              f'Следующиая отправка через {self.__send_period} секунд')

    def events_count(self):
        """
        Получение информации о числе собранных событий
        :return:
        """
        print(f'С сервера {self.__dst_ip_addr} собрано {self.count} событий')

    def clear_cache(self):
        """
        Очистка кэша событий
        :return:
        """
        self.count = 0
        print('Кеш агента был очищен')

    @property
    def collect_period(self):
        return self.__collect_period

    @collect_period.setter
    def collect_period(self, new_value):
        if '-' in new_value:
            raise ValueError("Значение не должно быть отрицательным")
        if 'h' in new_value:
           if 'm' in new_value:
               if 's' in new_value:
                    new_value = new_value.rstrip('s')
                    new_value_hours, new_value_tmp = new_value.split('h')
                    new_value_minutes, new_value_seconds = new_value_tmp.split('m')
                    new_value_in_seconds = ((int(new_value_hours) * 3600) +
                                            (int(new_value_minutes) * 60) + int(new_value_seconds))
               else:
                   new_value = new_value.rstrip('m')
                   new_value_hours, new_value_minutes = new_value.split('h')
                   new_value_in_seconds = ((int(new_value_hours) * 3600) + (int(new_value_minutes) * 60))
           else:
               if 's' in new_value:
                    new_value = new_value.rstrip('s')
                    new_value_hours, new_value_seconds = new_value.split('h')
                    new_value_in_seconds = (int(new_value_hours) * 3600) + int(new_value_seconds)
               else:
                    new_value_hours = new_value.rstrip('h')
                    new_value_in_seconds = int(new_value_hours) * 3600
        else:
            if 's' in new_value:
                new_value = new_value.rstrip('s')
                if 'm' in new_value:
                    new_value_minutes, new_value_seconds = new_value.split('m')
                    new_value_in_seconds = (int(new_value_minutes) * 60) + int(new_value_seconds)
                else:
                    new_value_in_seconds = int(new_value)
            else:
                new_value = new_value.rstrip('m')
                new_value_in_seconds = int(new_value) * 60
        self.__collect_period = new_value_in_seconds

def main():
    agent = MetricsAgent('100.100.100.10', '111-123', 10, 20)

    print(agent.collect_period)
    agent.collect_period = '1h30m30s'
    print(agent.collect_period)


if __name__ == '__main__':
    main()

