
if __name__ == '__main__':
    rps_values = (5081, '17184', 10968, 9666, '9102', 12321, '10617', 11633, 5035, 9554, '10424', 9378, '8577',
                  '11602', 14116, '8066', '11977', '8572', 9685, 11062, '10561', '17820', 16637, 5890, 17180, '17511',
                  '13203', 13303, '7330', 7186, '10213', '8063', '12283', 15564, 17664, '8996', '12179', '13657', 15817,
                  '16187', '6381', 8409, '5177', 17357, '10814', 6679, 12241, '6556', 12913, 16454, '17589', 5292,
                  '13639', '7335', '11531', '14346', 7493, 15850, '12791', 11288)

    i = 0
    rps_values_list = list(rps_values)

    while i in range(len(rps_values_list)):
        rps_values_list[i] = int(rps_values_list[i])
        i = i+1

    rps_values_list.sort()

    rps_value_avg = int(sum(rps_values_list) / len(rps_values_list))

    print('average value is ', rps_value_avg)

    #моё вычисление

    if (len(rps_values_list) % 2 == 0):
        mean_high_id = int(len(rps_values_list) / 2)
        mean_low_id = mean_high_id - 1
        rps_value_mean = int((rps_values_list[mean_low_id] + rps_values_list[mean_high_id]) / 2)
        print('mean value is ', rps_value_mean)

    else:
        mean_id = (len(rps_values_list) // 2)
        rps_value_mean = rps_values_list[mean_id]
        print('mean value is ', rps_value_mean)


    if (abs(rps_value_avg - rps_value_mean)) > 0.3 * (rps_value_mean):
        if rps_value_avg < rps_value_mean:
            print('Снижения')
        elif rps_value_avg > rps_value_mean:
            print('Скачки')
    else:
        print('Стабильная')

    # вычисление из курса

    quotient, remainder = divmod(len(rps_values_list), 2)
    median = rps_values_list[quotient] if remainder else sum(rps_values_list[quotient - 1: quotient + 1]) / 2

    print(median)

