if __name__ == '__main__':
    branch_name = input()
    tests_result = int(input()) # как сдлать хитрее с bool или ограничением только двумя значениями?
    coverage_change = float(input())
    approve_number = int(input())

    if ('development' in branch_name.lower()) or ('staging' in branch_name.lower()):
        if (tests_result == 1) and (coverage_change > 5):
            print(f'Внимание! Код из {branch_name} отправлен в релиз!')
        elif (tests_result == 1) and (coverage_change <= 5):
            if approve_number > 3:
                print(f'Внимание! Код из {branch_name} отправлен в релиз!')
            else:
                print(f'Код из {branch_name} с результатами тестов: {tests_result}, '
                      f'coverage: {coverage_change}, approve: {approve_number} в релиз не попадает.')
        else:
            print(f'Код из {branch_name} с результатами тестов: {tests_result}, '
                  f'coverage: {coverage_change}, approve: {approve_number} в релиз не попадает.')
    else:
        print(f'В ветке {branch_name} непроверенный код, пропускаем')
