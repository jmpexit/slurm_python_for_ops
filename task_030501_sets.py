#set

m = {'Julie', 'Julie', 'Jim'}
print(m)  # {'Julie', 'Jim'}

m.add('Jane')  # добавляет 1 элемент
print(m)  # {'Jane', 'Jim', 'Julie'}

m.update([1, 2])  # расширяет последовательностью
print(m)  # {1, 2, 'Julie', 'Jane', 'Jim'}

m.clear()
print(m)

my_set = {1, 2, 3, 4, 5}
my_set.remove(5)  # hard удаление
print(my_set)  # {1, 2, 3, 4}
#my_set.remove(6)  # исключение KeyError: 6

my_set.discard(6)  # safe удаление
print(my_set)  # {1, 2, 3, 4}

e = my_set.pop()
print(e, my_set)  # 1 {2, 3, 4}

my_superset = {1, 2, 3, 4, 5, 6, 7, 8, 9}
my_subset = {2, 3, 4}

print(my_subset.issubset(my_superset))  # True
print(my_superset.issuperset(my_subset))  # True

my_subset_two = my_subset.copy()
print(my_subset_two)  # {2, 3, 4}

my_subset.remove(2)
print(my_subset)  # {3, 4}
print(my_subset_two)  # {2, 3, 4}

print(my_superset.intersection(my_subset))  # {3, 4}
print(my_superset.difference(my_subset))  # {1, 2, 5, 6, 7, 8, 9}

first_set = {1, 2, 3, 4, 5}
second_set = {1, 2, 3, 6, 7}
print(first_set.symmetric_difference(second_set))  # {4, 5, 6, 7}
print(first_set.union(second_set))  # {1, 2, 3, 4, 5, 6, 7}