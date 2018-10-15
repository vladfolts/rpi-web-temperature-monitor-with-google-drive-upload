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

def test_list_dates(with_sample_db):
    assert with_sample_db[0].list_dates() == ['2018-09-16']

def test_trim(with_sample_db):
    db = with_sample_db[0]
    db.trim('2018-09-16')
    assert db.list_dates() == ['2018-09-16']

    # non-existing date
    db.trim('2018-09-16')

def test_trim_before(with_sample_db):
    db = with_sample_db[0]
    db.trim('2018-09-17')
    assert db.list_dates() == []

def test_trim_after(with_sample_db):
    db = with_sample_db[0]
    db.trim('2018-09-15')
    assert db.list_dates() == []

def test_before_only(with_two_dates_in_sample_db):
    db = with_two_dates_in_sample_db[0]
    assert db.list_dates() == ['2018-10-14', '2018-09-16']

    db.trim('2018-09-15', before_only=True)
    assert db.list_dates() == ['2018-10-14', '2018-09-16']

    db.trim('2018-09-16', before_only=True)
    assert db.list_dates() == ['2018-10-14', '2018-09-16']

    db.trim('2018-10-11', before_only=True)
    assert db.list_dates() == ['2018-10-14']
