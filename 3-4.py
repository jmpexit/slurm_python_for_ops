# Инициализация словаря
info_about_me = {"name": "Julie", "temperature": 29, "humidity": 53}

# Получение значения
print(info_about_me["name"])

# Добавление значения
info_about_me["is_i_love_python"] = False
print(info_about_me)

# Перезапись значения
info_about_me["humidity"] = 50
print(info_about_me)

# Метод метод безопасного получения значения get : если ключ отсутствует, получим не ошибку, а None
print(info_about_me.get("temperature_2"))

# get с установкой дефолтного значения
print(info_about_me.get("temperature_2", 25))

# Метод items (всё содержимое, пары ключ-значение) с приведением к списку
print(list(info_about_me.items()))

for k, v in info_about_me.items():
        print(k, v, sep=": ") #распаковываем кортеж

#Метод keys - все ключи
print(list(info_about_me.keys()))

#Метод values - все значения
print(list(info_about_me.values()))

# Метод update - расширяет/обновляет словарь
info_about_me.update({"temperature": 26, "cat_count": 1})
print(info_about_me)

# Метод popitem - вернет последнюю пару ключ-значение (и вырежет из словаря)
pair = info_about_me.popitem()
print(pair)
print(info_about_me)

# Метод pop - удаляет по указанному ключу и сохранит значение в переменную
value = info_about_me.pop("humidity")
print(value)
print(info_about_me)

# приравнивание двух словарей сделает их одновременно изменяемыми
info_about_me_2 = info_about_me
info_about_me_2["cat_count"] = 0

# Метод copy
info_about_me_3 = info_about_me.copy()
info_about_me_3["cat_count"] = 2
print(info_about_me)
print(info_about_me_2)
print(info_about_me_3)

# Метод setdefault: если в словаре есть указанный ключ, он вернется;
# если нет - создастся с указанным значением
value = info_about_me.setdefault("surname", "Naumov")
print(value)
print(info_about_me)

# Метод fromkeys: позволяет создать новый словарь из последовательности с ключами
my_dict = dict.fromkeys(["first", "second", 3], "hello I'm fromkeys")
print(my_dict)

# Создание словаря из последовательности
my_list = [("first", 1), ("second", 2), ("third", 3)]
print(dict(my_list))

# Создание словаря из отдельных последовательностей ключей и значений
my_keys = ["first", "second", "third"]
my_values = [1, 2, 3]
print(list(zip(my_keys, my_values)))
print(dict(zip(my_keys, my_values)))

# Метод clear
#info_about_me.clear()
#print(info_about_me)
