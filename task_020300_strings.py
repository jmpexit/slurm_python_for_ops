name = 'Julie'
job = 'QA'
email = 'glkg@dfgkdlgk.io'
who_am_i = name + ', ' + job #конкатинация
who_am_i_two = 'My name is {}, I am a {}, send your messages to {}'.format(name, job, email) #интерполяция, встраиваем одну строку в другую
who_am_i_three = 'My name is {nm}, I am a {jb}, send your messages to {em}'.format(nm=name, jb=job, em=email)
who_am_i_four = f'My name is {name}, {{}} I am a {job}, send your messages to {email}' #f-strings, сразу распознают существующие переменные
who_am_i_old = f'My name is %s, I am a %s, send your messages to %s' % (name, job, email) #в старых версиях языка; не используем
my_name_formatted = f'My name is {name:>30}' #форматирование
print(who_am_i)
print(who_am_i_two)
print(who_am_i_three)
print(who_am_i_four)
print(who_am_i_old)
print(my_name_formatted)

pod_name = "Pod"
replicaset_name = "Replicaset"
kubernetes_structures_desc = "Для объединения нескольких контейнеров в одну минимальную логическую единицу используется, в то время как контролирует количество реплик приложения"
kubernetes_structures_desc_inter = f'Для объединения нескольких контейнеров в одну минимальную логическую единицу используется {pod_name}, в то время как {replicaset_name} контролирует количество реплик приложения'
print(kubernetes_structures_desc_inter)