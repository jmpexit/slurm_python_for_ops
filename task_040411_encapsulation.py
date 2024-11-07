# Инкапсуляция — это скрытие прямого доступа к члену класса


class Slurmik():

    def __init__(self, name: str, profession: str, experience: int):
        """
        Конструктор
        :param name: Имя слёрмика
        :param profession: профессия слёрмика
        :param experience: стаж слёрмика
        """
        self.__name = name
        self.__profession = profession
        self.__experience = experience

    def say_hello(self):
        """
        Приветствует программиста
        :return:
        """
        print(f"Привет! Я слёрмик {self.__name}. Я {self.__profession}, мой стаж {self.__experience} лет.")

    # # не канонично для python
    # def get_name(self):
    #     return self.__name

    @property
    def name(self):
        return self.__name

    # # не канонично для python
    # def set_name(self, new_value):
    #     if len(new_value) <= 0 or not isinstance(new_value, str):  # not type(new_value) == str лучше не использовать
    #         raise ValueError("Имя должно быть непустой строкой")
    #     self.__name = new_value

    @name.setter
    def name(self, new_value):
        #if len(new_value) <= 0 or not isinstance(new_value, str):
        if not isinstance(new_value, str) or len(new_value) <= 0: # если одно из  «or» не было выполнено, то второе проверяться не будет
            raise ValueError("Имя должно быть непустой строкой")
        self.__name = new_value

def main():
    slurmik_vanya = Slurmik("Иван", "DevOps engineer", 14)
    slurmik_masha = Slurmik("Маша", "DevOps engineer", 10)

    # print(slurmik_vanya.get_name())
    # slurmik_vanya.set_name("Ivan")
    # print(slurmik_vanya.get_name())

    print(slurmik_vanya.name)
    slurmik_vanya.name = 'Ваня'
    print(slurmik_vanya.name)


if __name__ == '__main__':
    main()


