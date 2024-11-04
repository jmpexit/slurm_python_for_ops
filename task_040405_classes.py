class Slurmik(): # объявление класса
    """
    Существо слёрмик
    """

    def __init__(self, name: str, profession: str, experience: int): # аргументы конструктора
        # self дает возможность обращаться к членам класса внутри него
        """
        Конструктор
        :param name: Имя слёрмика
        :param profession: профессия слёрмика
        :param experience: стаж слёрмика (в годах)
        """
        # тело конструктора. объявление членов класса
        # __ - означает приватную обдасть видимсоти членов и методов класса (внутри класса).
        # _ - защищенная (внутри класса и его наследников)
        # без подчеркивания - публичкая, можно обращаться через объект
        self.__name = name
        self.__profession = profession
        self.__experience = experience

    def say_hello(self):
        """
        Приветствует программиста
        :return:
        """
        print(f"Привет! Я слёрмик {self.__name}. Я {self.__profession}, мой стаж {self.__experience} лет.")
        # self. - ссылка на сам класс, по имени обращаемся к члену класса

    def __change_experience(self, new_value: int, reason: str):
        """
        Смена стажа
        :param new_value: новый стаж (в годах)
        :param reason: причина смены стажа
        :return:
        """
        print(f"Слёрмик {self.__name} сменил стаж {self.__experience} на {new_value}. Причина: {reason}")
        self.__experience = new_value

    def convert_experience_to_mercury_years(self):
        """
        Переезд на Меркурий и смена стажа на меркурианские года
        :return:
        """
        self.__change_experience(self.__experience * (365 // 88), 'Переезд на Меркурий')


def main():
    fedia_slurmik = Slurmik('Фёдор', 'куа', 1)
    masha_slurmik = Slurmik('Маша', 'девопс', 7)

    #fedia_slurmik.__change_experience(2, "просто так") - не сможем выполнить,т.к. он защищен от внешнего вмешательства

    fedia_slurmik.convert_experience_to_mercury_years()

    #fedia_slurmik.__name = 'Федя'
    #print(fedia_slurmik.__name)
    # если сделать переменную класса name Закрытой (__name), мы все равно сможем ее изменить

    masha_slurmik.say_hello()
    fedia_slurmik.say_hello() # TODO почему тут принтуется Фёдор, когда присваиваешь __name = 'Федя'?

if __name__ == '__main__':
    main()
