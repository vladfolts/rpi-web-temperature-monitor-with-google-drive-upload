import storer

import os

def test_sqlite3_storer():
    db_dir = '_out'
    db_path = os.path.join(db_dir, 'test.db')
    if os.path.exists(db_path):
        os.remove(db_path)
    elif not os.path.exists(db_dir):
        os.mkdir(db_dir)

    s = storer.Sqlite3Storer(db_path)
    s.put(storer.Record(timestamp=1537131014.495, value=25.67))
    s.put(storer.Record(timestamp=1537131015, value=26))