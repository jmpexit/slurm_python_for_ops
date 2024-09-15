
def extent_and_prepare_list_with_new_values_from_input(mylist):
    """
    Получение доп. значений rps и приведение списка к сортированному списку целых значений
    :param mylist: список rps
    :return: возвращает сортированный список целых значений, включая введенные в строке ввода
    """
    map(int, mylist)
    while True:
        print('Введите значение RPS (через ;), введите отрезок выборки (в формате [N, M]) '
              'или нажмите Enter для продолжения')
        input_data = input()
        sli = False
        if input_data.isdigit():
            mylist.append(int(input_data))
            print(mylist)
        elif ';' in input_data:
            mylist.extend(map(int, input_data.split(';')))
            print(mylist)
        elif ']' in input_data:
            input_slice = input_data.strip('[]')
            input_values = list(map(int, input_slice.split(',')))
            print(input_values)
            mylist = mylist[input_values[0]:input_values[1]]
            sli = True
        elif input_data == '':
            break
        else:
            print('Валидация не пройдена')
        mylist = list(map(int, mylist))
        mylist.sort()
    print(mylist)
    return mylist


def calculate_avg_rps(mylist):
    """
    Считает среднее значение rps из списка
    :param mylist: список rps
    :return: среднее значение rps из списка
    """
    rps_value_avg = int(sum(mylist) / len(mylist))
    print('average value is ', rps_value_avg)
    return rps_value_avg

def calculate_mean_rps(mylist):
    """
    Считает медианное значение rps из списка
    :param mylist: список rps
    :return: медианное значение rps из списка
    """
    if (len(mylist) % 2 == 0):
        mean_high_id = int(len(mylist) / 2)
        mean_low_id = mean_high_id - 1
        rps_value_mean = int((mylist[mean_low_id] + mylist[mean_high_id]) / 2)
        print('mean value is ', rps_value_mean)
    else:
        mean_id = (len(mylist) // 2)
        rps_value_mean = mylist[mean_id]
        print('mean value is ', rps_value_mean)
    return rps_value_mean

def suggest_stability_rste(rps_value_avg, rps_value_mean):
    """
    Вывод о характере нагрузки на основе средних и медианных значений rps:
    Происходят снижения, Происходят скачки, Нагрузка стабильна
    :param rps_value_avg: среднее значение rps
    :param rps_value_mean: медианное значение rps
    :return:
    """
    if (abs(rps_value_avg - rps_value_mean)) > 0.25 * (rps_value_mean):
        if rps_value_avg < rps_value_mean:
            print('Происходят снижения')
        elif rps_value_avg > rps_value_mean:
            print('Происходят скачки')
    else:
        print('Нагрузка стабильна')


def main():
    rps_values_list = ['11531', '14346', 7493, 15850, '12791', 11288]
    rps_values_list = extent_and_prepare_list_with_new_values_from_input(rps_values_list)
    avg_rps = calculate_avg_rps(rps_values_list)
    mean_rps = calculate_mean_rps(rps_values_list)
    suggest_stability_rste(avg_rps, mean_rps)


main()