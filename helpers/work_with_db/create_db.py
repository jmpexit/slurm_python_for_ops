import sqlite3


def create_database():
    con = sqlite3.connect('../../commands.db')
    con.close()

    # OR
    # with sqlite3.connect("my.db") as conn:
    #     # interact with database
    #     pass

DB_CREDS = {"database": "commands.db"}
