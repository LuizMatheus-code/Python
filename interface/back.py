import sqlite3 as sq

dbase = sq.connect('employee_records.db')
c = dbase.cursor()
dbase.execute(''' CREATE TABLE IF NOT EXISTS employee_records(
                ID INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL)''')
dbase.commit()


def write(ID, NAME):
    c.execute(''' INSERT into employee_records(ID, NAME) VALUES(?, ?)''', (ID, NAME))
    dbase.commit()
