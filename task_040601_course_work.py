def main():

if __name__ == "__main__":
    main()


# устанивливаем requirements
# запускаем monitoring module через терминал python monitoring_module.py
# модуль работает на порту 21122
# в файле monitoring module находим эедпоинт:
    # @app.route("/monitoring/infrastructure/using/summary/<int:company_branch>")
# смотрим, что на нем curl 127.0.0.1:21122/monitoring/infrastructure/using/summary/1
    # 1 - тут любое число, говорит о повторяемости значений (можно выбирать 2, 3... , чтобы значения генератора менялись)




