import sqlite3

DB_CREDS = {"database": "example.db"}


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
        print("Connection was closed")

def main():
    with DBAccessor(DB_CREDS) as cursor:
        for row in cursor.execute("SELECT * FROM user"):
            print(row)

    #AAA debug
    print("AAA") # тут, после выхода на уровень с with, уже будет выполнен __exit__


if __name__ == "__main__":
    main()