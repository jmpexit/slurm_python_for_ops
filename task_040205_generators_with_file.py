# Вариант с обычными циклами
#
def read_file_generator(file_name):
    with open(file_name) as log_file: # контекстный менеджер. сам позаботится о закрытии файла
        for row in log_file:
            yield row

            # вместо конструкции     log_file = open(file_name) -> log_file.close()

def main():
    for row in read_file_generator("log.txt"):
        if row.lower().startswith('error'):
        #         if row.lower().__contains__('error'):
            print(row)


if __name__ == '__main__':
    main()

# yield Делает функцию генератором. Позволяет вернуть из функции результат,
# обработать его вне функции и вернуться в функцию за новым результатом.