# Вариант с обычными циклами
#
# def generate_seq(max_v=5000):
#     values = []  # объем списка может быть таким большим , что не поместится в оперативку
#     for number in range(0, max_v + 1):
#         values.append(number)
#     return values
#
#
# def main():
#     for number in generate_seq():
#         if number % 12 == 0:
#             print(number)


# # Вариант с генератором 1
# #
# def generate_seq(max_v=5000):
#     for number in range(0, max_v + 1):
#         yield number  # делает из функции генератор
#
#
# def main():
#     values = []
#     for number in generate_seq():
#         if number % 12 == 0:
#             values.append(number)
#     print(values)

# Вариант с генератором 2
#
def generate_seq(max_v=100):
    for number in range(0, max_v + 1):
        yield number  # делает из функции генератор


def add_two(value):  # доп. функция для наглядности
    return str(value + 2)


def main():
    # comprehension. можно применять к спискам и словарям
    values = [
        number
        for number in generate_seq()
        if number % 12 == 0
    ]
    #[add_two(number): for number in generate_seq() if number % 12 == 0]
    #values = {add_two(number): number for number in generate_seq() if number % 12 == 0}
    print(values)


if __name__ == '__main__':
    main()

