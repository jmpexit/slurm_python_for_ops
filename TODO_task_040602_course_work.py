#     Первый элемент в скобках - ID ресурса
#     Второй элемент в скобках - Измерение ресурса (CPU, RAM или NetFlow)
#     Третий элемент в скобках - Дата и время сбора статистики
#     Четвертый элемент в скобках - Загрузка ресурса в процентах (от 0 до 100)

#data = input()
data = ('cmd1|(ID1, type1, date1, load1);(ID2, type2, date2, load2)'
        '$cmd3|(ID3, type3, date3, load3)'
        '$cmd4|(ID4, type4, date4, load4)')


# {'Название команды':
#   {'Название ресурса':
#       {'Измерение ресурса':
#           {'Среднее измерения': 51.645, 'Медиана измерения': 53.0, 'Тип использования': 'Stable', 'Интенсивность использования': 'Medium',
# 'envisioneer rich mindshare':
#    {'SZY1417':
#        {'CPU':
#           {'mean': 51.645, 'mediana': 53.0, 'usage_type': 'Stable', 'intensivity': 'Medium'}
# ... }

def parse_commands(input_data):
    commands_and_resources = []
    commands_parsed = []
    resources_parsed = []
    commands_and_resources_dict = {}
    for i in range(0, (input_data.count('$')+1)):
        if '$' in input_data:
            commands, input_data = input_data.split('$', 1)
            #new idea
            #commands_and_resources, input_data = input_data.split('$', 1)
            # потом для каждой команды - список нескольких ресурсов в подцикле
        else:
            commands = input_data
        command, resources = commands.split('|', 1)
        commands_parsed.append(command)
        #commands_and_resources.append('{' + '\'' + command + '\'' + ': ')
        for i in range(0, (resources.count(',') + 1)):
            if ',' in resources:
                resource, resources = resources.split(',', 1)
            else:
                resource = resources
            resource = resource.strip('(),')
            resources_parsed.append(resource)
            #commands_and_resources.append('{' + '\'' + resource + '\'' + ': ')
            #print(resource)
    print(commands_parsed)
    print(resources_parsed)
    commands_and_resources_dict = dict(zip(commands_parsed, resources_parsed))
    commands_and_resources_dict.
    print(commands_and_resources_dict)

    # old example:
    # ip_addresses = ips.translate({ord(i): None for i in '[]"\''}).split(', ')
    # commands = cmds.translate({ord(i): None for i in '[]"\''}).split(', ')

    # print(commands_and_resources)
    # for command in commands_and_resources:
    #     if ';' in command:
    #         command, temp_value = command.split(';', 1)
    #     else:
    #         command = input_data
    #     commands_and_resources.append(command)



#cmd|(ID, Измерение, Дата, Загрузка);(ID, Измерение, Дата, Загрузка)$cmd|(ID, Измерение, Дата, Загрузка)

        # if 'm' in new_value:
        #     minutes, new_value = new_value.split('m', 1)
        #     new_value_in_seconds += int(minutes) * 60
        # if 's' in new_value:
        #     new_value = new_value.rstrip('s')
        #     new_value_in_seconds += int(new_value)
        # return new_value_in_seconds

def main():
    #data = input()
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


