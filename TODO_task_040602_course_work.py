#     Первый элемент в скобках - ID ресурса
#     Второй элемент в скобках - Измерение ресурса (CPU, RAM или NetFlow)
#     Третий элемент в скобках - Дата и время сбора статистики
#     Четвертый элемент в скобках - Загрузка ресурса в процентах (от 0 до 100)

#data = input()
data = ('cmd1|(ID1, type1, date1, load1);(ID2, type2, date2, load2)'
        '$cmd3|(ID3, type3, date3, load3)'
        '$envisioneer rich mindshare|(SZY1417, CPU, 2024-12-12 13:00, 50)')


# {'Название команды': {'Название ресурса': {'Измерение ресурса': {'Среднее измерения': 51.645, 'Медиана измерения': 53.0, 'Тип использования': 'Stable', 'Интенсивность использования': 'Medium',
# 'envisioneer rich mindshare': {'SZY1417': {'CPU': {'mean': 51.645, 'mediana': 53.0, 'usage_type': 'Stable', 'intensivity': 'Medium'} ... }
# 'envisioneer rich mindshare': {'SZY1417': {'CPU': {'mean': 51.645, 'mediana': 53.0, 'usage_type': 'Stable', 'intensivity': 'Medium'} ... }

def parse_commands(input_data):
    commands_and_resources = []
    commands_parsed = []
    resources_parsed = []
    commands_and_resources_dict = {}
    for i in range(0, (input_data.count('$')+1)):
        if '$' in input_data:
            command_line, input_data = input_data.split('$', 1)
        else:
            command_line = input_data
        command, resources = command_line.split('|', 1)
        commands_parsed.append(command)
        resources = resources.translate({ord(i): None for i in '()'})
        resources_parsed.append(resources)

    commands_and_resources_dict = dict(zip(commands_parsed, resources_parsed))

    print('')

    for k, v in commands_and_resources_dict.items():
        v_new = set()
        for i in range(0, (v.count(';') + 1)):
            if ';' in v:
                v1, v = v.split(';', 1)
                v_new.add(v1)
            else:
                v_new.add(v)
        v = v_new
        commands_and_resources_dict.update({k: v})

    for k, v in commands_and_resources_dict.items():
       v_res = dict()

       for i in v:
            res_id, scope, date, load = i.split(',')
            print(res_id, scope, date, load)
            v_res.update({res_id: {scope, date, load}})

       commands_and_resources_dict.update({k: v_res})


    print('')
    print(commands_and_resources_dict)


def main():
    parse_commands(data)


if __name__ == "__main__":
    main()

    # Название команды|(Ресурс,Измерение ресурса,Дата и время сбора статистики,Загрузка ресурса);
    # (Ресурс,Измерение ресурса,Дата сбора статистики,Загрузка ресурса)$Название команды|
    # (Ресурс,Измерение ресурса,Дата сбора статистики,Загрузка ресурса);
    #
    # Команды и описание их ресурсов отделяются при помощи разделителя "$"
    # Название команды от ресурсов команды отделяется при помощи разделителя "|"
    # Ресурсов команды перечислены в круглых скобках и отделяются при помощи разделителя ";"
    #     Первый элемент в скобках - ID ресурса
    #     Второй элемент в скобках - Измерение ресурса (CPU, RAM или NetFlow)
    #     Третий элемент в скобках - Дата и время сбора статистики
    #     Четвертый элемент в скобках - Загрузка ресурса в процентах (от 0 до 100)
    # Требуется произвести парсинг данной последовательности

    # {'Название команды': {'Название ресурса': {'Измерение ресурса': {'Среднее измерения': 51.645, 'Медиана измерения': 53.0, 'Тип использования': 'Stable', 'Интенсивность использования': 'Medium',
    # 'envisioneer rich mindshare': {'SZY1417': {'CPU': {'mean': 51.645, 'mediana': 53.0, 'usage_type': 'Stable', 'intensivity': 'Medium'}
    # ...
    # }

    # usage_type - тип нагрузки: скачки, стабильная, и снижения
    # intensivity - интенсивность использования: низкая, умеренная, высокая, запредельная
    # Таким образом получаются состояния

    # Также помимо словаря, нужно создать текстовый отчет по каждой команде, в котором нужно отобразить использование их ресурсов.
    #
    # Например по каждой команде может быть создана таблица (данные в таблице рандомные, и не соответствуют условиям задания):
    #
    # |Resource|Dimension|mean|mediana|usage_type|intensivity|decision|
    # |APT-323|CPU|56|47.0|Stable|Low|delete resource|
    # |APT-323|RAM|74|43.0|Stable|Medium|normal using|
    # |DHH-HW1|RAM|52.56|55.5|Stable|Extreme|extend resource|


