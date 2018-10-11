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
def with_sample_db(with_empty_dir):
    db_path = os.path.join(with_empty_dir, 'sample.db')
    s = storer.Sqlite3Storer(db_path)
    s.put(storer.Record(timestamp=1537131014.49, value=25.67))
    s.put(storer.Record(timestamp=1537131015, value=26))
    return s, db_path

def remove_if_exists(path):
    if os.path.exists(path):
        os.remove(path)

