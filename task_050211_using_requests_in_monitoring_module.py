import sqlite3
import requests

# запускаем monitoring module через терминал: python monitoring_module.py

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
#               '(7-6317O,RAM,2025-02-09 01:10:31,67);(7-6317O,RAM,2025-02-09 02:10:31,65)'
#               '$implement open-source bandwidth|(SBP 366,CPU,2025-02-08 11:56:36,39);'
#               '(SBP 366,CPU,2025-02-08 12:56:36,60);(SBP 366,CPU,2025-02-08 13:56:36,47);'
#               '(SBP 366,CPU,2025-02-08 15:56:36,53);(SBP 366,CPU,2025-02-08 16:56:36,35);(SBP 366,CPU,2025-02-08 17:56:36,48);'
#               '(SBP 366,CPU,2025-02-09 12:56:36,60);(SBP 366,CPU,2025-02-09 13:56:36,39);(SBP 366,CPU,2025-02-09 14:56:36,37);'
#               '(SBP 366,CPU,2025-02-10 03:56:36,39);(SBP 366,CPU,2025-02-10 04:56:36,52)$strategize world-class web services|'
#               '(32A 892,CPU,2025-02-08 11:56:36,8);(32A 892,CPU,2025-02-08 12:56:36,4);(32A 892,CPU,2025-02-08 13:56:36,6);'
#               '(32A 892,CPU,2025-02-08 14:56:36,17);(32A 892,CPU,2025-02-08 15:56:36,23);'
#               '(32A 892,CPU,2025-02-09 01:56:36,13);(32A 892,CPU,2025-02-09 02:56:36,10);'
#               '(32A 892,CPU,2025-02-09 03:56:36,14)$drive revolutionary infrastructures|(NBX-4230,CPU,2025-02-08 11:56:36,33);'
#               '(NBX-4230,CPU,2025-02-08 13:56:36,0);(NBX-4230,CPU,2025-02-08 14:56:36,99);(NBX-4230,CPU,2025-02-08 15:56:36,99);'
#               '(NBX-4230,CPU,2025-02-08 16:56:36,4);(NBX-4230,CPU,2025-02-08 17:56:36,2);(NBX-4230,CPU,2025-02-08 18:56:36,0);'
#               '(NBX-4230,CPU,2025-02-08 19:56:36,0);(NBX-4230,CPU,2025-02-08 20:56:36,99);(NBX-4230,CPU,2025-02-08 21:56:36,0);'
#               '(NBX-4230,CPU,2025-02-08 22:56:36,20);(NBX-4230,CPU,2025-02-08 23:56:36,0);(NBX-4230,CPU,2025-02-09 00:56:36,99);'
#               '(NBX-4230,CPU,2025-02-09 01:56:36,0);(NBX-4230,CPU,2025-02-09 02:56:36,17)')


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
        command_name = command_name.replace(' ', '_').replace('-', '_')
        commands.update({"command_name": command_name})
        for resource in resource_info.split(';'):
            resource = resource[1:-1]
            resource = resource.split(',', 6)  # make it a list
            res_name, res_type, res_time, mean, mediana = resource[0], resource[1], resource[2], resource[3], resource[3]
                    #TODO !!!!!!!! NOT update !!!!!!!!!
            resources.update({"res_name": res_name, "res_type": res_type, "res_time": res_time, "mean": mean, "mediana": mediana,
                                      "stability": count_resource_stability(mean, mediana), "intensity": count_resource_intensity(mediana),
                                      "decision": make_a_decision_about_resource(count_resource_stability(mean, mediana),
                                                                                 count_resource_intensity(mediana))})
            #commands.setdefault(command_name, []).append(resources)

            with DBAccessor(DB_CREDS) as cursor:
                cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {command_name} (
                ResourceId INTEGER PRIMARY KEY,
                ResourceName TEXT NOT NULL,
                Scope TEXT NOT NULL,
                ResTime TEXT,
                Mean INTEGER,
                Mediana INTEGER,
                UsageType TEXT,
                Intensity TEXT,
                Decision TEXT
                )
                ''')

                cursor.execute(f'INSERT INTO {command_name} (ResourceName, Scope, ResTime, Mean, Mediana, UsageType, Intensity, Decision) '
                                   f'VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                                       (resources["res_name"], resources["res_type"], resources["res_time"], resources["mean"],
                                        resources["mediana"],resources["stability"], resources["intensity"], resources["decision"]))
                                       #('MOCK_name', 'MOCK_type', 50, 50, 'MOCK_usage_type', 'MOCK_intensity', 'MOCK_decision',))
                #print(f'Writing data into {command} table')
                # for row in cursor.execute(f'SELECT * FROM {command}'):
                #     print(row)

        commands[resource_info] = resources


def main():
    parse_commands_and_save_to_db(input_data)

if __name__ == "__main__":
    main()

