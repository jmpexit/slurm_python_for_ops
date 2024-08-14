
one = 1.0
slurm = 'Slurm'
loc_slurm = 'Слёрм'

print(type(one) != type(slurm))
print(not type(one) == type(slurm))
print(type(loc_slurm) == type(slurm))
print(loc_slurm == slurm)

#NOTE: переменные, содержащие логическое значение, лучше называть с
# is_ или  has_

is_python_easy = True
print(not is_python_easy)

my_name = "Хикматилло"
print(ord(my_name[0]))  # 1061
#is_my_name_long = ord(my_name[0]) > 8 # выдаст исключение, т.к. оператор не работает с разными типами
is_my_name_long = my_name == 8
print(is_my_name_long)

# step 2-4-10
# TODO: Написать программу, которая будет определять, является ли приложение отказоустойчивым
free_ram_amount = 200  # Количество свободной оперативной памяти в облачном кластере в мегабайтах
app_replicas = 2 # Количество реплик приложения
has_ram_overdraft = True # Есть ли возможность использовать дополнительную оперативную память при исчерпании лимита
balance = 7000  # Баланс лицевого счета в местной валюте

is_enough_money = (balance >= 8000)

is_stable = (app_replicas > 1) * (((free_ram_amount / app_replicas) >= 150) + (has_ram_overdraft * (balance >= 8000)))
print((app_replicas > 1) and (((free_ram_amount / app_replicas) >= 150) or bool(has_ram_overdraft and (balance >= 8000))))





