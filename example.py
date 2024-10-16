# print("я example")
#
# print(f"{__name__=}")
#
# print("Код на уровне модуля")
#
# if __name__ == "__main__":
#     print("Код за точкой входа")
#
#     #  запустить напрямую python example.py
#     #  запустить python main.py

def a():
    print('111')
    yield 1
    print('22')
    yield 2
    print('33')
    yield 3
    print('44')

b = a()
print(next(b))
print(next(b))
print(next(b))
print(next(b))