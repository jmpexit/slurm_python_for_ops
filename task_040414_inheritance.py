# Инкапсуляция — это скрытие прямого доступа к члену класса


class Slurmik:

    def __init__(self, name: str, profession: str, experience: int):
        """
        Конструктор
        :param name: Имя слёрмика
        :param profession: профессия слёрмика
        :param experience: стаж слёрмика
        """
        self._name = name # для примера сделаем скрытым и не будем использовать геттер-сеттер
        self.__profession = profession
        self.__experience = experience

    def say_hello(self):
        """
        Приветствует программиста
        :return:
        """
        print(f"Привет! Я слёрмик {self._name}. Я {self.__profession}, мой стаж {self.__experience} лет.")


    # @property
    # def name(self):
    #     return self.__name
    #
    # @name.setter
    # def name(self, new_value):
    #     if not isinstance(new_value, str) or len(new_value) <= 0: # если одно из  «or» не было выполнено, то второе проверяться не будет
    #         raise ValueError("Имя должно быть непустой строкой")
    #     self.__name = new_value


# class SlurmikDev(Slurmik):
#     def write_program(self, code_row_count):
#         print(f"Я {self.name} и я пишу программу из {code_row_count} строк кода на питоне")

# также можно перетащить конструктор родительского класса
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
        self.__lang = lang

    def write_program(self, code_row_count):
        print(f"Я {self._name} и я пишу программу из {code_row_count} строк кода на {self.__lang}")


def main():
    slurmik_vanya = Slurmik("Иван", "DevOps engineer", 14)
    slurmik_masha = SlurmikDev("Даша", "Developer", 10, 'C#')


    print(slurmik_masha._name)  # Но так делать ни в коем случае не стоит !!!
    slurmik_masha._name = 'Маша'
    print(slurmik_masha._name)
    slurmik_masha.write_program(20)
    slurmik_vanya.say_hello()
    slurmik_masha.say_hello()

if __name__ == '__main__':
    main()


