# TODO: Вывести строку с интерполированными переменными +
# TODO: Убрать пробелы в начале и в конце имени +
# TODO: Убрать символы “~” в начале и конце имени +
# TODO: Сделать первую букву имени заглавной +
# TODO: Привести профессию к нижнему регистру +
# TODO: Заменить в адресе электронной почты символ “@ на предлог “at” +
# TODO: Разгадать и вывести секретный символ

name = "       ~~~daniel~~     "
job = "R&D dEvElOpEr"
email = "d.naumov@slurm.io"
secret_symbol_first_part = "wer4605rtrt"
secret_symbol_second_part = "w5g3t3g2j"
secret_symbol = chr(int(secret_symbol_first_part[3:7]) + int(secret_symbol_second_part[1:9:2]))

# chr - извлекает символ по его коду, ord - по символу плучает его код

name_fixed = name.strip(' ~').capitalize()
job_fixed = job.lower()
email_fixed = email.replace('@', ' at ')


my_string = (f'Hi! My name is {name_fixed}, I am a {job_fixed}, '
             f'send your messages to {email_fixed}{secret_symbol}')

print(my_string)
print(ord('⛑'))

#step 13

# TODO: привести к виду Минимальной единицей Kubernetes является pod
platform = "K8s"
atomic_unit = "POD"
what_about_kubernetes = f"Минимальной единицей {platform.replace('8', 'ubernete')} является {atomic_unit.lower()}"
print(what_about_kubernetes)

#step 15

# TODO: При помощи срезов необходимо извлечь из строки следующие подстроки: "recovery", "recovery plan", "Disaster"

instruction_name = "Disaster recovery plan"

print(instruction_name[9:-5])
print(instruction_name[9:])
print(instruction_name[:8])





