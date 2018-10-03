#from fixture import with_sample_db

import os

def test_sqlite3_storer(with_sample_db):
    assert os.path.exists(with_sample_db)