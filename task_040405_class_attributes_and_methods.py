class Slurmik():

    specialization = 'K8S grandmaster'  # переменная класса (не объекта). будет находиться у всех объектов класса

    @classmethod  # декоратор
    def tell_about_specialization(cls):  # cls : ссылка не на текущий объект, а на текущий класс
        print(f'Моя специализация - {cls.specialization}')

    @staticmethod  # статический метод. не принимает ничего, просто что-то делает, например, вывод константы
    def slurmik_static_method():
            print('I am a static method')

    """
    Существо слёрмик
    """

    def __init__(self, name: str, profession: str, experience: int):
        """
        Конструктор
        :param name: Имя слёрмика
        :param profession: профессия слёрмика
        :param experience: стаж слёрмика (в годах)
        """
        self.__name = name
        self.__profession = profession
        self.__experience = experience


def main():
    fedia_slurmik = Slurmik('Фёдор', 'куа', 1)
    masha_slurmik = Slurmik('Маша', 'девопс', 7)

    print(masha_slurmik.specialization)
    print(fedia_slurmik.specialization)
    print('-' * 15)

    Slurmik.specialization = 'Docker grandmaster'

    print(masha_slurmik.specialization)
    print(fedia_slurmik.specialization)
    print('-' * 15)

    #fedia_slurmik.specialization = 'QA grandmaster'

    print(masha_slurmik.specialization)
    print(fedia_slurmik.specialization)
    print('-' * 15)

    Slurmik.specialization = 'Engeneering grandmaster'

    print(masha_slurmik.specialization)
    print(fedia_slurmik.specialization) # ! тут останется "QA grandmaster", т.к. у конкретного объекта уже изменен
    print('-' * 15)

    Slurmik.tell_about_specialization()
    masha_slurmik.tell_about_specialization()
    fedia_slurmik.tell_about_specialization() # но тут будет новая 'Engeneering grandmaster'.
    # дело в том, что в tell_about_specialization(cls) мы обращаемся к переменной класса,
    # а в fedia_slurmik.specialization мы СОЗДАЛИ НОВЫЙ ЧЛЕН КЛАССА для Феди !
    print('-' * 15)

    # Более наглядно :
    fedia_slurmik.specialization_2 = 'Kafka grandmaster'

    print(fedia_slurmik.specialization)
    print(fedia_slurmik.specialization_2)
    print(masha_slurmik.specialization)
    print('-' * 15)

    # ВАЖНО! если при обращении к переменной (напр. fedia_slurmik.specialization) переменная ОБЪЕКТА не нашлась,
    # она будет искаться на уровне КЛАССА

    # выполнение статического метода
    Slurmik.slurmik_static_method()


if __name__ == '__main__':
    main()


