#from fixture import with_sample_db

import os

def test_sqlite3_storer(with_sample_db):
    db_path = with_sample_db[1]
    assert os.path.exists(db_path)

def test_list_gen(with_sample_db):
    storer = with_sample_db[0]
    assert [(r.timestamp, r.value) for r in storer.list_gen()] == [(1537131015, 26), (1537131014.49, 25.67)]

def test_list_gen_limit(with_sample_db):
    storer = with_sample_db[0]
    assert [(r.timestamp, r.value) for r in storer.list_gen(limit=1)] == [(1537131015, 26)]    

    storer = with_sample_db[0]
    assert [(r.timestamp, r.value) for r in storer.list_gen(limit=10)] == [(1537131015, 26), (1537131014.49, 25.67)]