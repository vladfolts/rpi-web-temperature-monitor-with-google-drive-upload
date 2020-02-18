import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import storer

import pytest
import shutil
import time

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
def with_sample_db(with_empty_db, sample_date1_ts_1, sample_date1_ts_2):
    s = with_empty_db[0]
    s.put(storer.Record(timestamp=sample_date1_ts_1, value=25.67))
    s.put(storer.Record(timestamp=sample_date1_ts_2, value=26))
    return with_empty_db

@pytest.fixture
def sample_date1_ts_1():
    return 1537131014.49 # Sep 16 15:50:14 2018

@pytest.fixture
def sample_date1_ts_2():
    return 1537131015 # Sep 16 15:50:15 2018

@pytest.fixture
def sample_date2_ts_1():
    return 1539561879.77 # Oct 14 19:04:39 2018

@pytest.fixture
def sample_date2_ts_2():
    return 1539561880.77 # Oct 14 19:04:40 2018

@pytest.fixture
def sample_day_before_date1_ts_1(sample_date1_ts_1):
    return sample_date1_ts_1 - 24 * 60 * 60

@pytest.fixture
def sample_day_before_date2_ts_1(sample_date2_ts_1):
    return sample_date2_ts_1 - 24 * 60 * 60

@pytest.fixture
def sample_day_after_date1_ts_1(sample_date1_ts_1):
    return sample_date1_ts_1 + 24 * 60 * 60

@pytest.fixture
def sampe_local_date_str_1(sample_date1_ts_1):
    return _ts_to_local_date_str(sample_date1_ts_1)

@pytest.fixture
def sampe_local_date_str_2(sample_date2_ts_1):
    return _ts_to_local_date_str(sample_date2_ts_1)

@pytest.fixture
def sampe_local_day_before_date_str_1(sample_day_before_date1_ts_1):
    return _ts_to_local_date_str(sample_day_before_date1_ts_1)

@pytest.fixture
def sampe_local_day_before_date_str_2(sample_day_before_date2_ts_1):
    return _ts_to_local_date_str(sample_day_before_date2_ts_1)

@pytest.fixture
def sampe_local_day_after_date_str_1(sample_day_after_date1_ts_1):
    return _ts_to_local_date_str(sample_day_after_date1_ts_1)

@pytest.fixture
def with_two_dates_in_sample_db(with_empty_dir, with_sample_db, sample_date2_ts_1, sample_date2_ts_2):
    s = with_sample_db[0]
    s.put(storer.Record(timestamp=sample_date2_ts_1, value=26))
    s.put(storer.Record(timestamp=sample_date2_ts_2, value=25.67))
    return s, with_sample_db[1]

def remove_if_exists(path):
    if os.path.exists(path):
        os.remove(path)

def _ts_to_local_date_str(ts):
    return time.strftime('%Y-%m-%d', time.localtime(ts))