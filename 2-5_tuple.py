
trashbin = ('Julie', 'Msc', True, 0)
myname, city, is_true, animals_count = trashbin

climate = (24, 50)

print(is_true)

print(trashbin + climate)

animals_count2, temperature, humidity = (trashbin + climate)[3:] #срез результата конкатинации

print(animals_count2, temperature, humidity)

name = 'Bob'
a, b, c = name

print(a)

cor = ("Слёрм",)

basic_courses = ("Docker", "Ansible", "Ceph")
advanced_courses = ("Kubernetes База", "Kubernetes Мега")

print((basic_courses + advanced_courses)[1::3])