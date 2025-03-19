# https://habr.com/ru/articles/104086/
# использоавать консольный дебаггер: python3 -m pdb {имя скрипта}.py
# step - след.функция, list - несколько строк до и после, list {номер строки},
# break {номер строки} - установить брейкпоинт, disable {порядк.номер брекпоинта} - удалить бп,
# cont - выполнить программу до брейкпоинта, p {переменная} - распечатать переменную
# help - список всех команд pdb, bt - почледний бектрейс, ...
# exec("raise ValueError") - выбросить исключение

def get_email_and_job_from_input():
    """
    Получение почты и профессии сотрудника из потока вывода
    :return: почты и профессии сотрудника
    """
    print("Введите email")
    email = input()
    if email == "":
        print("Ввод прерван")
        return None, None
    print("Введите профессию")
    job = input()
    return email, job # возвращаем кортеж, но без скобок: особенность return


def get_system_info(job):
    """
    Получение информации о системе для доступа
    :param job: Название должности
    :return: система доступа и кол-во попыток для выдачи прав
    """
    if job == "Программист":
        return "CKB", 1
    elif job == "Дизайнер":
        return "Иллюстратор", 3
    else:
        print("АХО через три двери направо")
        return None, None

def get_access_details_from_input():
    """
    Получение даты открытия доступа и периода доступа из потока
    ввода
    :return: даты открытия доступа и период доступа
    """
    print("Введите дату открытия доступа")
    access_from = input()
    print("Введите период доступа (в днях)")
    access_period = int(input())

    # try:
    #     access_period = int(access_period)
    # except ValueError:
    #     return None, None
    # finally:
    #     print(f'Дата открытия дотсупа - {access_from}, период - {access_period}')

    return access_from, access_period


def allow_access_to_user(email, system, access_attempts):
    """
    Выдача права в систему
    :param email: Почта сотрудника
    :param system: Название системы
    :param access_attempts: Количество попыток для выдачи прав
    :return:
    """
    for _ in range(access_attempts):
        print(f"{email} был выдан доступ в {system}")


def main():
    processed_employees = 0
    employees_no = 2
    while processed_employees < employees_no:
        email, job = get_email_and_job_from_input()
        if email is None and job is None:
            break

        access_from, access_period = get_access_details_from_input()
        if access_from is None and access_period is None:
            print('Неанрно введены данные')
            continue

        system, access_attempts = get_system_info(job)

        if system is None and access_attempts is None:
            allow_access_to_user(email, access_details=(1,access_from, access_period), system="sanitary_engineering_room")
            continue

        allow_access_to_user(email, access_attempts=access_attempts, system=system)
        processed_employees += 1
        print(f"Было внесено {processed_employees} сотрудников, осталось {employees_no - processed_employees}")


if __name__ == '__main__':
    main()