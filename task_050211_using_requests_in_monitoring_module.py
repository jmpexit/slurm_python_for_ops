import sqlite3
import requests

# запускаем monitoring module через терминал python monitoring_module.py

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
        self.__connection.commit()
        self.__connection.close()
        print('')
        print("Connection was closed")


def get_monitoring_data():
    base_url = 'http://127.0.0.1:21122/monitoring/infrastructure/using/summary/1'
    input_data = requests.get(base_url)

    return input_data.text

input_data = get_monitoring_data()
# input_data = ('envisioneer rich mindshare|(SZY1417,CPU,2025-02-08 11:10:31,7);'
#               '(SZY1417,CPU,2025-02-08 12:10:31,83);(SZY1417,CPU,2025-02-08 13:10:31,53);'
#               '(SZY1417,NetFlow,2025-02-09 11:10:31,64);(SZY1417,NetFlow,2025-02-09 12:10:31,43);'
#               '(7-6317O,RAM,2025-02-09 01:10:31,67);(7-6317O,RAM,2025-02-09 02:10:31,65);'
#               '(7-6317O,RAM,2025-02-09 03:10:31,38)')



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

def parse_commands_and_save_to_db(raw_input_data):
    commands = {}
    resources = {}
    for command_info in raw_input_data.split('$'):
        command_name, resource_info = command_info.split('|')
        command_name = command_name.replace(' ', '_')
        commands.update({"command_name": command_name})

        #for command in command_name:


        for resource in resource_info.split(';'):
            resource = resource[1:-1]
            resource = resource.split(',', 5)  # make it a list
            res_name, res_type, stat_time, mean, mediana = resource[0], resource[1], resource[2], resource[3], resource[3]
                #TODO !!!!!!!! NOT update !!!!!!!!!
            resources.update({"res_name": res_name, "res_type": res_type, "mean": mean, "mediana": mediana,
                                  "stability": count_resource_stability(mean, mediana), "intensity": count_resource_intensity(mediana),
                                  "decision": make_a_decision_about_resource(count_resource_stability(mean, mediana),
                                                                             count_resource_intensity(mediana))})
            commands.setdefault(command_name, []).append(resources)

            with DBAccessor(DB_CREDS) as cursor:
                cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {command_name} (
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

                cursor.execute(f'INSERT INTO {command_name} (ResourceName, Scope, Mean, Mediana, UsageType, Intensity, Decision) '
                                   f'VALUES (?, ?, ?, ?, ?, ?, ?)',
                                   (resources["res_name"], resources["res_type"], resources["mean"], resources["mediana"],
                                   resources["stability"], resources["intensity"], resources["decision"]))
                                   #('MOCK_name', 'MOCK_type', 50, 50, 'MOCK_usage_type', 'MOCK_intensity', 'MOCK_decision',))
                    #print(f'Writing data into {command} table')
            break
                    # for row in cursor.execute(f'SELECT * FROM {command}'):
                    #     print(row)

        # commands[resource_info] = resources


    return commands

def main():
    parse_commands_and_save_to_db(input_data)
    #print(commands)


if __name__ == "__main__":
    main()
    #print(input_data)
