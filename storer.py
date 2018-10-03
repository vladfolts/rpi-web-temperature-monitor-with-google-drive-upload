import os
import sqlite3

def _create_db_schema(conn):
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE temperature (rowid INTEGER PRIMARY KEY AUTOINCREMENT, timestamp REAL, value REAL)')
    conn.commit()

class Record(object):
    def __init__(self, timestamp, value):
        self.timestamp = timestamp
        self.value = value

db_name = 'data.db'

class Sqlite3Storer(object):
    def __init__(self, db_name=db_name):
        existed = os.path.exists(db_name)
        self.__conn = sqlite3.connect(db_name)
        if not existed:
            _create_db_schema(self.__conn)

    def put(self, record):
        cursor = self.__conn.cursor()
        cursor.execute('INSERT INTO temperature(timestamp, value) VALUES(%s, %s)' % (record.timestamp, record.value))
        self.__conn.commit()