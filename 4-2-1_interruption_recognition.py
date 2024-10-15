# TODO (d.naumov): Если почта пользователя на домене slurm.io - уведомлять и завершать программу
# TODO (d.naumov): Генерировать список email для их создания на новых доменах

COMPANIES = ["southbridge.ru", "universe.slurm.io"]  # большими буквами обычно обозначают гдобальные переменные,
                                                    # значения которых далее в программе менять не следует

USERS = ["d.krivosheev@slurm.io", "a.egorov@slurm.io", "a.gorina@slurm.io", "d.naumov@notslurm.io",
         "a.amantaeva@slurm.io", "v.vostrikova@slurm.io", "y.alvarez@test.io"]

if __name__ == '__main__':
    new_email = []

    for domain in COMPANIES:
        for email in USERS:
            login, old_domain = email.split("@")
            if old_domain != "slurm.io":
                print(f'Почтовый адрес {email} не в корпоративном домене')
                break
            new_email.append(login + '@' + domain)
        else:  # ! else на уровне for: выполнится, только если ни разу не отработает break
            continue
        break
    else:
        print('Данные провалидированы')
        print(new_email)