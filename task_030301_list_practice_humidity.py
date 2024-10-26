

if __name__ == '__main__':
    workroom_humidity = [42, 46, 39, 47, 53, 48, 42, 39, 40]

    while True:
        print('Введите влажность')
        input_data = input()
        if input_data.isdigit():
            workroom_humidity.append(int(input_data))
            print(workroom_humidity)
        elif ',' in input_data:
            workroom_humidity.extend(map(int, input_data.split(',')))
            # map - применяет тип ко всем значениям последовательности
            print(workroom_humidity)
        elif input_data == '':
            break
        else:
            print('Валидация не пройдена')

    workroom_humidity.sort()
    print(workroom_humidity)
    humidity_outlier = workroom_humidity.pop()
    print(humidity_outlier)

    sum_of_humidity = 0
    for humidity in workroom_humidity:
        sum_of_humidity += humidity

    for i in range(1, 6, 2): #только четные
        print(i, sum_of_humidity / len(workroom_humidity))