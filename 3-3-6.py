
if __name__ == '__main__':
    rps_values_list = ['11531', '14346', 7493, 15850, '12791', 11288]

    map(int, rps_values_list)

    while True:
        print('Введите значение RPS')
        input_data = input()
        sli = False
        if input_data.isdigit():
            rps_values_list.append(int(input_data))
            print(rps_values_list)
        elif ';' in input_data:
            rps_values_list.extend(map(int, input_data.split(';')))
            print(rps_values_list)
        elif ']' in input_data:
            input_slice = input_data.strip('[]')
            input_values = list(map(int, input_slice.split(',')))
            print(input_values)
            rps_values_list = rps_values_list[input_values[0]:input_values[1]]
            print(rps_values_list)
            sli = True
        elif input_data == '':
            break
        else:
            print('Валидация не пройдена')

    rps_values_list = list(map(int, rps_values_list))
    rps_values_list.sort()
    print(rps_values_list)

    rps_value_avg = int(sum(rps_values_list) / len(rps_values_list))

    print('average value is ', rps_value_avg)

    if (len(rps_values_list) % 2 == 0):
        mean_high_id = int(len(rps_values_list) / 2)
        mean_low_id = mean_high_id - 1
        rps_value_mean = int((rps_values_list[mean_low_id] + rps_values_list[mean_high_id]) / 2)
        print('mean value is ', rps_value_mean)

    else:
        mean_id = (len(rps_values_list) // 2)
        rps_value_mean = rps_values_list[mean_id]
        print('mean value is ', rps_value_mean)

    if (abs(rps_value_avg - rps_value_mean)) > 0.25 * (rps_value_mean):
        if rps_value_avg < rps_value_mean:
            print('Происходят снижения')
        elif rps_value_avg > rps_value_mean:
            print('Происходят скачки')
    else:
        print('Нагрузка стабильна')
