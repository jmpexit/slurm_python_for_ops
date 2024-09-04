

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

        system, access_attempts = get_system_info(job)
        if system is None and access_attempts is None:
            allow_access_to_user(email, access_attempts=1, system="Инженерная")
            continue

        allow_access_to_user(email, access_attempts=access_attempts, system=system)
        processed_employees += 1
        print(f"Было внесено {processed_employees} сотрудников, осталось {employees_no - processed_employees}")


if __name__ == '__main__':
    main()
