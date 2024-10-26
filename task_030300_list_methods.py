my_list = [1, 2, 3]
my_list.append('four') #добавить в конец
my_list.extend([5, 6, 7]) #расширить другим списком
my_list.pop() #извлечь последний из конца

print(my_list)

my_list_copy = my_list.copy()
print(my_list_copy)

my_list.reverse()
print()
print(my_list)
print(my_list_copy)

# my_list.sort(reverse=True)
# print(my_list)

my_list.clear()
print()
print(my_list)
print(my_list_copy)
