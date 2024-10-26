

def work_with_mutables(my_list):
    my_list[2].append(6)
 #   my_list.append(7)


def main():
    my_other_list = [1, 2, [3, 4, 5]]
    my_other_tuple = (1, 2, [3, 4, 5])
    work_with_mutables(my_other_list)
    work_with_mutables(my_other_tuple)

    print(my_other_list, '\n', my_other_tuple)


main()

def work_with_mutables_default(my_list = []):  # не надо так (= функция - это также объект,
                                            # внутри нее хранится объект по умолчанию и будет изменяться
    my_list.append(3)
    print(my_list)


def main2():
    for _ in range(6):
        work_with_mutables_default()

main2()

# [3]
# [3, 3]
# [3, 3, 3]
# [3, 3, 3, 3]
# [3, 3, 3, 3, 3]
# [3, 3, 3, 3, 3, 3]

# instead :

def work_with_mutables_none(my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(3)
    print(my_list)


def main3():
    for _ in range(6):
        work_with_mutables_none()

main3()


def main4():
    foo = work_with_mutables_none  # взятие функтора
    foo()  # вызов через переменную

main4()