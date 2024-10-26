
COMPANIES = ["southbridge.ru", "universe.slurm.io"]

USERS = ["d.krivosheev@slurm.io", "a.egorov@slurm.io", "a.gorina@slurm.io", "d.naumov@notslurm.io",
         "a.amantaeva@slurm.io", "v.vostrikova@slurm.io", "y.alvarez@test.io"]

if __name__ == '__main__':
    new_email = []

    for domain in COMPANIES:
        for email in USERS:
            if not email.endswith("slurm.io"):
                break
            print(email)
        else:
            continue
        break

#  При выполнении условия прерывания во внутреннем цикле будет вызвана инструкция break
#  Инструкция else во внутреннем цикле отследит было ли вызвано прерывание внутреннего цикла при помощи инструкции break
#  Если было вызвано прерывание внутреннего цикла при помощи инструкции break, итерация внешнего цикла НЕ завершится досрочно
#  Так как итерация внешнего цикла НЕ завершится досрочно, то внешний цикл будет остановлен при помощи инструкции break
