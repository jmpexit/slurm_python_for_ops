import sqlite3


def create_database():
    con = sqlite3.connect('../commands.db')
    con.close()

    # OR
    # with sqlite3.connect("my.db") as conn:
    #     # interact with database
    #     pass

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
        # метод будет вызываться тогда, когда мы выйдем из области видимости контекстного менеджера
        self.__connection.commit()
        self.__connection.close()
        print('')
        print("Connection was closed")


# def create_table():
#     with DBAccessor(DB_CREDS) as cursor:
#         cursor.execute(f'''
#         CREATE TABLE IF NOT EXISTS command (
#         ResourceId INTEGER PRIMARY KEY,
#         ResourceName TEXT NOT NULL,
#         Scope TEXT NOT NULL,
#         Mean INTEGER,
#         Mediana INTEGER,
#         UsageType TEXT,
#         Intensity TEXT,
#         Decision TEXT
#         )
#         ''')
#
#         cursor.execute(f'INSERT INTO command (ResourceName, Scope, Mean, Mediana, UsageType, Intensity, Decision) '
#                         'VALUES (?, ?, ?, ?, ?, ?)',
#                         ('MOCK_name', 'MOCK_scope', 50, 50, 'MOCK_usage_type', 'MOCK_intensity', 'MOCK_decision',))
#
#         for row in cursor.execute(f'SELECT * FROM command'):
#             print(row)
#
#
# def drop_table():
#     with DBAccessor(DB_CREDS) as cursor:
#         cursor.execute('DROP table IF EXISTS cmd1')
#         cursor.execute('DROP table IF EXISTS cmd3')
#         cursor.execute('DROP table IF EXISTS envisioneer_rich_mindshare')
#     print('')
#     print('Tables have been deleted')
#
#
def main():
    create_database()


if __name__ == "__main__":
    main()
