import sqlite3

con = sqlite3.connect('example.db')

# with con:
#     con.execute("""
#         create table user (
#             id varchar(10) primary key,
#             name varchar(50)
#             );
#     """)

data = [('0001', 'Julie'), ('0002', 'Johnny'), ('0003', 'Jackie'), ('0004', 'Rouge')]

sql = 'insert into user (id, name) values (?, ?)'

with con:
     con.executemany(sql, data)