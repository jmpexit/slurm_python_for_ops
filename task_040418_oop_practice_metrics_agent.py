#TODO Агент для Prometheus не позволяет управлять периодом отправки событий

def parse_time(time):
    if '-' in time:
        raise ValueError("Значение не должно быть отрицательным")
    new_value_in_seconds = 0
    if 'h' in time:
        hours, time = time.split('h', 1)
        new_value_in_seconds += int(hours) * 3600
    if 'm' in time:
        minutes, time = time.split('m', 1)
        new_value_in_seconds += int(minutes) * 60
    if 's' in time:
        time = time.rstrip('s')
        new_value_in_seconds += int(time)
    return new_value_in_seconds

class MetricsAgent:
    """
    Агент сбора метрик
    """
    count = 0

    def __init__(self, dst_ip_addr: str, access_key: str, collect_period: int, send_period: str):
        """
        Конструктор
        :param dst_ip_addr: IP адрес сервера, к которому подключается агент
        :param access_key: ключ доступа к серверу
        :param collect_period: период сбора метрик (в секундах)
        :param send_period: период отправки событий на сервер сбора событий (в секундах)
        """
        self._dst_ip_addr = dst_ip_addr
        self._access_key = access_key
        self._collect_period = collect_period
        self._send_period = send_period

    def collect_events(self):
        """
        Сбор событий
        :return:
        """
        print(f'События сервера {self._dst_ip_addr} собраны. Следующий сбор через {self._collect_period} секунд')

    def send_events(self):
        """
        Отправка событий
        :return:
        """
        self.count += 1
        print(f'События сервера {self._dst_ip_addr} собраны и отправлены на сервер сбора метрик. '
              f'Следующиая отправка через {self._send_period} секунд')

    def events_count(self):
        """
        Получение информации о числе собранных событий
        :return:
        """
        print(f'С сервера {self._dst_ip_addr} собрано {self.count} событий')

    def clear_cache(self):
        """
        Очистка кэша событий
        :return:
        """
        self.count = 0
        print('Кеш агента был очищен')


class MetricsAgentCarbon(MetricsAgent):
    """
    Агент сбора метрик Carbon
    """
    count = 0

    def __init__(self, dst_ip_addr: str, access_key: str, collect_period: int, send_period: str, carbon_ip_addr: str):
        """
        Конструктор
        :param dst_ip_addr: IP адрес сервера, к которому подключается агент
        :param access_key: ключ доступа к серверу
        :param collect_period: период сбора метрик (в секундах)
        :param send_period: период отправки событий на сервер сбора событий (в секундах)
        """
        super().__init__(dst_ip_addr, access_key, collect_period, send_period)
        self.carbon_ip_addr = carbon_ip_addr

    def send_events(self):
        """
        Отправка событий
        :return:
        """
        self.count += 1
        print(f'События сервера {self._dst_ip_addr} собраны и отправлены в Carbon. '
              f'Следующиая отправка через {self._send_period} секунд')

    @property
    def collect_period(self):
        return self._collect_period

    @collect_period.setter
    def collect_period(self, new_value):
        def parse_time(new_value):
            if '-' in new_value:
                raise ValueError("Значение не должно быть отрицательным")
            new_value_in_seconds = 0
            if 'h' in new_value:
                hours, new_value = new_value.split('h', 1)
                new_value_in_seconds += int(hours) * 3600
            if 'm' in new_value:
                minutes, new_value = new_value.split('m', 1)
                new_value_in_seconds += int(minutes) * 60
            if 's' in new_value:
                new_value = new_value.rstrip('s')
                new_value_in_seconds += int(new_value)
            return new_value_in_seconds
        self._collect_period = parse_time(new_value)

    @property
    def send_period(self):
        return self._send_period

    @send_period.setter
    def send_period(self, new_value):
        def parse_time(new_value):
            if '-' in new_value:
                raise ValueError("Значение не должно быть отрицательным")
            new_value_in_seconds = 0
            if 'h' in new_value:
                hours, new_value = new_value.split('h', 1)
                new_value_in_seconds += int(hours) * 3600
            if 'm' in new_value:
                minutes, new_value = new_value.split('m', 1)
                new_value_in_seconds += int(minutes) * 60
            if 's' in new_value:
                new_value = new_value.rstrip('s')
                new_value_in_seconds += int(new_value)
            return new_value_in_seconds
        self._send_period = parse_time(new_value)


class MetricsAgentPrometheus(MetricsAgent):
    """
    Агент сбора метрик Prometheus
    """
    count = 0

    def __init__(self, dst_ip_addr: str, access_key: str, collect_period: int, send_period: str):
        """
        Конструктор
        :param dst_ip_addr: IP адрес сервера, к которому подключается агент
        :param access_key: ключ доступа к серверу
        :param collect_period: период сбора метрик (в секундах)
        :param send_period: период отправки событий на сервер сбора событий (в секундах)
        """
        super().__init__(dst_ip_addr, access_key, collect_period, send_period)
        self._send_period = parse_time(send_period)

    def send_events(self):
        """
        Отправка событий
        :return:
        """
        self.count += 1
        print(f'События сервера {self._dst_ip_addr} собраны и отправлены  по запросу от Prometheus.')

    @property
    def collect_period(self):
        return self._collect_period

    @collect_period.setter
    def collect_period(self, new_value):
        def parse_time(new_value):
            if '-' in new_value:
                raise ValueError("Значение не должно быть отрицательным")
            new_value_in_seconds = 0
            if 'h' in new_value:
                hours, new_value = new_value.split('h', 1)
                new_value_in_seconds += int(hours) * 3600
            if 'm' in new_value:
                minutes, new_value = new_value.split('m', 1)
                new_value_in_seconds += int(minutes) * 60
            if 's' in new_value:
                new_value = new_value.rstrip('s')
                new_value_in_seconds += int(new_value)
            return new_value_in_seconds
        self._collect_period = parse_time(new_value)

def main():
    agent_ca = MetricsAgentCarbon('100.100.100.10', '111-123', 10, '20', '100.100.100.11')
    agent_p = MetricsAgentPrometheus('100.100.100.12', '111-124', 10, '60h1s')

    print(agent_ca.collect_period)
    agent_ca.collect_period = '60h1s'
    agent_ca.send_period = '60h1s'
    agent_p.collect_period = '60h1s'
    agent_p.send_period = '60h1s'
    print(agent_ca.collect_period, agent_ca.send_period, agent_p.collect_period, agent_p.send_period, agent_ca.carbon_ip_addr)

    agent_ca.collect_events()
    agent_ca.send_events()
    agent_p.send_events()
    agent_p.send_events()
    agent_p.events_count()
    agent_p.clear_cache()
    print(agent_p.send_period)

if __name__ == '__main__':
    main()

