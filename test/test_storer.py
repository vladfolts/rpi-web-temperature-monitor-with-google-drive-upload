import storer

import os

def test_sqlite3_storer(with_empty_db):
    db_path = with_empty_db[1]
    assert os.path.exists(db_path)

def test_put_none(with_empty_db):
    s = with_empty_db[0]
    s.put(storer.Record(timestamp=1537131015, value=None))
    assert [(r.timestamp, r.value) for r in s.list_gen()] == [(1537131015, None)]

def test_list_gen(with_sample_db):
    storer = with_sample_db[0]
    assert [(r.timestamp, r.value) for r in storer.list_gen()] == [(1537131015, 26), (1537131014.49, 25.67)]

def test_list_gen_limit(with_sample_db):
    storer = with_sample_db[0]
    assert [(r.timestamp, r.value) for r in storer.list_gen(limit=1)] == [(1537131015, 26)]    

    storer = with_sample_db[0]
    assert [(r.timestamp, r.value) for r in storer.list_gen(limit=10)] == [(1537131015, 26), (1537131014.49, 25.67)]

def test_list_dates(with_sample_db, sampe_local_date_str_1):
    assert with_sample_db[0].list_dates() == [sampe_local_date_str_1]

def test_trim(with_sample_db, sampe_local_date_str_1):
    db = with_sample_db[0]
    db.trim(sampe_local_date_str_1)
    assert db.list_dates() == [sampe_local_date_str_1]

    # non-existing date
    db.trim(sampe_local_date_str_1)

def test_trim_before(with_sample_db, sampe_local_day_after_date_str_1):
    db = with_sample_db[0]
    db.trim(sampe_local_day_after_date_str_1)
    assert db.list_dates() == []

def test_trim_after(with_sample_db, sampe_local_day_before_date_str_1):
    db = with_sample_db[0]
    db.trim(sampe_local_day_before_date_str_1)
    assert db.list_dates() == []

def test_before_only(
        with_two_dates_in_sample_db,
        sampe_local_day_before_date_str_1,
        sampe_local_date_str_1,
        sampe_local_day_before_date_str_2,
        sampe_local_date_str_2):
    db = with_two_dates_in_sample_db[0]
    assert db.list_dates() == [sampe_local_date_str_2, sampe_local_date_str_1]

    db.trim(sampe_local_day_before_date_str_1, before_only=True)
    assert db.list_dates() == [sampe_local_date_str_2, sampe_local_date_str_1]

    db.trim(sampe_local_date_str_1, before_only=True)
    assert db.list_dates() == [sampe_local_date_str_2, sampe_local_date_str_1]

    db.trim(sampe_local_day_before_date_str_2, before_only=True)
    assert db.list_dates() == [sampe_local_date_str_2]
