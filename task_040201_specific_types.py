from collections import deque, namedtuple, defaultdict, Counter

# frozenset - неизменяемое мн-во
# deque - двусвязный список (можно менять с обоих сторон)
# namedtuple - кортеж с именами членов
# OrderedDict - словарь, запоминающий порядок вставки (обычный словать в новом питоне делает так же)
# defaultdict - словарь, присв-щий дефолтное значение новым элементам, не имеющим еще значения
# Counter - словарь частот
# User<TypeName> - заготовка для создания своей реализации типа


def main():
    names = ['Valerie', 'Johnny', 'Judy', 'Johnny', 'Jackie']
    print(names)

    # frozenset
    frozen_names = frozenset(names)
    print(frozen_names)
    my_dict = {frozen_names: 1}
    print(my_dict)

    # deque
    deque_names = deque(names)
    print(deque_names)
    last_deque_value = deque_names.pop()
    deque_names.appendleft(last_deque_value)
    print(deque_names)

    # namedtuple
    Character = namedtuple('Characters', ('protagonist', 'antagonist', 'lover', 'choom', 'new_friend'))
    characters = Character(protagonist='Valerie',
                           antagonist='Johnny',
                           lover='Judy',
                           choom='Jackie',
                           new_friend='Johnny')
    print(characters)
    print(characters.lover)

    # defaultdict
    def default_name():
        return 'unknown_name'

    names_dict = defaultdict(default_name)
    names_dict['protagonist'] = 'Valerie'
    names_dict['lover']
    print(names_dict)

    # Counter
    name_count = Counter()
    name_count['Valerie'] += 1
    name_count['Jackie'] += 1
    name_count['Johnny'] += 1
    name_count['Johnny'] += 1
    name_count['Valerie'] += 1
    name_count['Valerie'] += 1
    name_count['Valerie'] += 1
    name_count['Johnny'] += 1
    name_count['Valerie'] += 1
    name_count['Valerie'] += 2
    name_count['Judy'] += 1
    name_count['Judy'] += 1
    name_count['Johnny'] += 2

    print(name_count)
    print(name_count.most_common(2))

if __name__ == '__main__':
    main()