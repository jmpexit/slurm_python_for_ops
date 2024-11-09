# Инкапсуляция — это скрытие прямого доступа к члену класса


class Slurmik:

    def __init__(self, name: str, profession: str, experience: int):
        """
        Конструктор
        :param name: Имя слёрмика
        :param profession: профессия слёрмика
        :param experience: стаж слёрмика
        """
        self._name = name
        self._profession = profession
        self._experience = experience

    def say_hello(self):
        """
        Приветствует программиста
        :return:
        """
        print(f"Привет! Я слёрмик {self._name}. Я {self._profession}, мой стаж {self._experience} лет.")


class SlurmikDev(Slurmik):
    def __init__(self, name: str, profession: str, experience: int, lang: str):
        """
        Конструктор
        :param name: Имя слёрмика
        :param profession: профессия слёрмика
        :param experience: стаж слёрмика
        :param lang: любимый ЯП
        """
        super().__init__(name, profession, experience) # нужно инициализировать родительский класс
        self._lang = lang

    def write_program(self, code_row_count):
        print(f"Я {self._name} и я пишу программу из {code_row_count} строк кода на {self._lang}")

    def say_hello(self):
        """
        Приветствует программиста
        :return:
        """
        print(f"Привет! Я слёрмик-программист {self._name}. Мой стаж программирования {self._experience} лет.")


def main():
    slurmik_vanya = Slurmik("Иван", "DevOps engineer", 14)
    slurmik_masha = SlurmikDev(" Маша", "Developer", 5, 'Python')
    slurmik_dima = SlurmikDev("Дима", "Developer", 10, 'C#')

    for slurmik in (slurmik_vanya, slurmik_masha, slurmik_dima):
        slurmik.say_hello()


if __name__ == '__main__':
    main()


