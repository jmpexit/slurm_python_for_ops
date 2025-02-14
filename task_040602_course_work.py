import sqlite3

DB_CREDS = {"database": "commands.db"}

class DBAccessor:
    def __init__(self, db_creds: dict):
        self.__db_creds = db_creds
        self.__connection = None
        self.__cursor = None

    def __enter__(self):
        print("Connection opening")
        if self.__connection is None:
            self.__connection = sqlite3.connect(**self.__db_creds)
        self.__cursor = self.__connection.cursor()
        return self.__cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        # метод будет у нас вызываться тогда,
        # когда мы выйдем из области видимости контекстного менеджера
        self.__connection.commit()
        self.__connection.close()
        print('')
        print("Connection was closed")

#     Первый элемент в скобках - ID ресурса
#     Второй элемент в скобках - Измерение ресурса (CPU, RAM или NetFlow)
#     Третий элемент в скобках - Дата и время сбора статистики
#     Четвертый элемент в скобках - Загрузка ресурса в процентах (от 0 до 100)

#input_data = input()
input_data = ('cmd1|(ID1, type1, date1, 50, 53);' # usage_type1, intensity1 - calculable
              '(ID2, type2, date2, 550, 70)'
        '$cmd3|(ID3, type3, date3, 30, 1000)'
        '$envisioneer rich mindshare|(SZY1417, CPU, 2024-12-12 13:00, 15, 23)') # Stable, Medium


# {'Название команды': {'Название ресурса': {'Измерение ресурса': {'Среднее измерения': 51.645, 'Медиана измерения': 53.0, 'Тип использования': 'Stable', 'Интенсивность использования': 'Medium',
# 'envisioneer rich mindshare': {'SZY1417': {'CPU': {'mean': 51.645, 'mediana': 53.0, 'usage_type': 'Stable', 'intensity': 'Medium'} ... }
# 'envisioneer rich mindshare': {'SZY1417': {'CPU': {'mean': 51.645, 'mediana': 53.0, 'usage_type': 'Stable', 'intensity': 'Medium'} ... }


def count_resource_stability(mean, mediana):
    if int(mean) < (0.75 * int(mediana)):
        return 'Falls'
    elif int(mean) > (1.25 * int(mediana)):
        return 'Peaks'
    else:
        return 'Stable'

def count_resource_intensity(mediana):
    if (int(mediana) > 0) and (int(mediana) <= 30):
        return 'Low'
    elif (int(mediana) > 30) and (int(mediana) <= 60):
        return 'Medium'
    else:
        return 'Extreme'


def make_a_decision_about_resource(stability: str, intensity: str): # METHOD IS CREATED BY AI!
    if intensity == 'Low':
        return "От такого ресурса нужно отказаться."
    elif intensity == 'Medium':
        if stability in ['Falls', 'Stable']:
            return "Такой ресурс остается у команды в неизменном виде."
        elif stability == 'Peaks':
            return "Такой ресурс остается у команды в неизменном виде."
    elif intensity == 'Extreme':
        if stability in ['Falls', 'Stable']:
            return "Такой ресурс остается у команды в неизменном виде."
        elif stability == 'Peaks':
            return "Такой ресурс остается у команды и его необходимо усилить."
    elif intensity == 'Extreme':
        return "Такой ресурс остается у команды и его необходимо усилить."
    else:
        return "Некорректные данные."



def parse_resources_info_method_one(raw_resources_info: str): # setdefault idea is obtained from course
    resource_properties = {}
    resource_scope = {}
    resources = {}
    for resource_info in raw_resources_info.split(';'):
        resource_info = resource_info[1:-1] # also replace may be used
        #res_name, res_type, stat_time, res_load, res_additional = resource_info.split(',', 4) # gives ValueError: not enough values to unpack (expected 5, got 4)
        #res_additional = [] if len(resource_info) == 5 else resource_info[-1].split(',') - if it has to be extended


        resource_info = resource_info.split(',', 5) # make it a list
        res_name, res_type, stat_time, mean, mediana  = resource_info[0], resource_info[1], resource_info[2], resource_info[3], resource_info[4]
        resource_properties.update({"mean": mean, "mediana": mediana,
            "stability": count_resource_stability(mean, mediana), "intensity": count_resource_intensity(mediana),
                                    "decision": make_a_decision_about_resource(count_resource_stability(mean, mediana), count_resource_intensity(mediana))})
        resource_scope.setdefault(res_type, []).append(resource_properties)
        #print(resource_scope)
        resources.setdefault(res_name, []).append(resource_scope)

    return resources


def parse_commands_method_one(raw_input_data: str):
    commands = {}
    resources = {}
    for command_info in raw_input_data.split('$'):
        command_name, resource_info = command_info.split('|')
        resources = parse_resources_info_method_one(resource_info)
        commands.setdefault(command_name, []).append(resources)
        print('')
    print(commands)
        #print(command_name[:100])
    #print(commands['cmd1'])

    return commands


def parse_commands_method_two(raw_input_data: str):
    commands = {}
    resources = {}
    for command_info in raw_input_data.split('$'):
        command_name, resource_info = command_info.split('|')
        commands.setdefault(command_name, [])
        #commands.update({"command_name": command_name})
        for resource in resource_info.split(';'):
            resource = resource[1:-1]
            resource = resource.split(',', 5)  # make it a list
            res_name, res_type, stat_time, mean, mediana = resource[0], resource[1], resource[2], resource[3], resource[4]
            resources.update({"res_name": res_name, "res_type": res_type, "mean": mean, "mediana": mediana,
                              "stability": count_resource_stability(mean, mediana), "intensity": count_resource_intensity(mediana),
                              "decision": make_a_decision_about_resource(count_resource_stability(mean, mediana),
                                                                         count_resource_intensity(mediana))})
        commands[command_name] = resources

    print(commands)
    print(commands['cmd1']['res_name'])

    return commands

def collect_data_into_database(command, resource_name, scope, mean, mediana, usage_type, intensity, decision):
    command = command.replace(' ', '_')
    with DBAccessor(DB_CREDS) as cursor:
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {command} (
        ResourceId INTEGER PRIMARY KEY,
        ResourceName TEXT NOT NULL,
        Scope TEXT NOT NULL,
        Mean INTEGER,
        Mediana INTEGER,
        UsageType TEXT,
        Intensity TEXT,
        Decision TEXT
        )
        ''')

        cursor.execute(f'INSERT INTO {command} (ResourceName, Scope, Mean, Mediana, UsageType, Intensity, Decision) '
                       f'VALUES (?, ?, ?, ?, ?, ?)', ({resource_name}, {scope}, {mean}, {mediana}, {usage_type}, {intensity}, {decision}))
                       # 'VALUES (?, ?, ?, ?, ?, ?)',
                       # ('MOCK_scope', 50, 50, 'MOCK_usage_type', 'MOCK_intensity', 'MOCK_decision',))
        print(f'Writing data into {command} table')

        for row in cursor.execute(f'SELECT * FROM {command}'):
            print(row)


def main():
    commands = parse_commands_method_two(input_data)

    # Write into database
    # for command in commands:
    #      collect_data_into_database(command["command_name"], command["res_name"], command["res_type"], command["mean"], command["mediana"], command["stability"], command["intensity"], command["decision"])

    # for command in commands:
    #     print(command['command_name'])

    #print(input_data[:100])


if __name__ == "__main__":
    main()
