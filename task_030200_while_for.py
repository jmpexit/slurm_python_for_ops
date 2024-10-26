if __name__ == '__main__':
    attempts = 0
    is_succeeded = False
    #while attempts < 10 and not is_succeeded:
    #    is_succeeded = retry()
    #    attempts +=1

    last_humidity = None # пока ничего не присваиваем

    while last_humidity is None:
        print('enter humidity')
        input_data = input()
        if input_data.isdigit():
            last_humidity = int(input_data)

    workroom_humidity = (42, 46, 39, 47, 53, 48, 42, 39, 40, last_humidity)


    for humidity in workroom_humidity:
        print(humidity)

    sum_of_humidity = 0
    for humidity in workroom_humidity:
        sum_of_humidity += humidity

    print('avg humidity', sum_of_humidity / len(workroom_humidity))

    for i in range(0, 6, 2): #только четные
        print(i, sum_of_humidity / len(workroom_humidity))