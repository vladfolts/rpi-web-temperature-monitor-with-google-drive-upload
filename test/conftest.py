import storer

import os
import pytest
import shutil

@pytest.fixture
def with_empty_dir():
    result = '_out'
    if os.path.exists(result):
        shutil.rmtree(result)
    os.mkdir(result)
    return result

@pytest.fixture
def with_empty_db(with_empty_dir):
    db_path = os.path.join(with_empty_dir, 'sample.db')
    s = storer.Sqlite3Storer(db_path)
    return s, db_path

@pytest.fixture
def with_sample_db(with_empty_db):
    s = with_empty_db[0]
    s.put(storer.Record(timestamp=1537131014.49, value=25.67))
    s.put(storer.Record(timestamp=1537131015, value=26))
    return with_empty_db

@pytest.fixture
def with_two_dates_in_sample_db(with_empty_dir, with_sample_db):
    s = with_sample_db[0]
    s.put(storer.Record(timestamp=1539561879.77, value=26))
    s.put(storer.Record(timestamp=1539561880.77, value=25.67))
    return s, with_sample_db[1]

def remove_if_exists(path):
    if os.path.exists(path):
        os.remove(path)

