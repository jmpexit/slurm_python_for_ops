
# устанивливаем requirements pip install -r requirements.txt
# запускаем monitoring module через терминал python monitoring_module.py
# модуль работает на порту 21122 - В консоли появится адрес и порт приложения
# Далее получаем данные при помощи команды curl localhost:21122/monitoring/infrastructure/using/summary/1

# в файле monitoring module также можно найти эедпоинт:
    # @app.route("/monitoring/infrastructure/using/summary/<int:company_branch>")
# смотрим, что на нем curl 127.0.0.1:21122/monitoring/infrastructure/using/summary/1
    # 1 - тут любое число, говорит о повторяемости значений (можно выбирать 2, 3... , чтобы значения генератора менялись)


def main():
    input_data = input()
    print(input_data[:100])

if __name__ == "__main__":
    main()


# чтобы передать результаты работы мониторинга, вводим во 2ом терминале
    # curl 127.0.0.1:21122/monitoring/infrastructure/using/summary/1 | python task_040601_course_work_monitoring_module.py