import backup
import storer

import os
import pytest
from mock import call, Mock

def test_backup(with_empty_dir, with_sample_db):
    output = os.path.join(with_empty_dir, 'backup.db')
    db_path = with_sample_db[1]
    backup.backup(db_path, output)
    assert os.path.exists(output)

def test_backup_can_overwrite_existing_backup(with_empty_dir, with_sample_db):
    test_backup(with_empty_dir, with_sample_db)
    test_backup(with_empty_dir, with_sample_db)

def test_backup_and_trim(
        with_two_dates_in_sample_db, 
        sampe_local_date_str_1, 
        sampe_local_date_str_2):
    db, db_path = with_two_dates_in_sample_db
    assert db.list_dates() == [sampe_local_date_str_2, sampe_local_date_str_1]

    uploaded = []
    backup.backup_and_trim(db_path, upload=lambda path: uploaded.append(path))
    assert uploaded == [os.path.join(os.path.dirname(db_path), '%s.db' % name) for name in \
        [sampe_local_date_str_2, sampe_local_date_str_1]]
    assert db.list_dates() == [sampe_local_date_str_2]

def test_backup_with_retry_tried_once_if_ok():
    backup_mock = Mock()
    backup.with_retry(backup_mock)
    backup_mock.assert_called_once_with()

def test_backup_with_retry():
    calls = {'count': 0}
    def fail_first_time():
        calls['count'] += 1
        count = calls['count']
        if count == 1:
            raise Exception('test')
        
    backup_mock = Mock(side_effect=fail_first_time)
    backup.with_retry(backup_mock, attempts=2)
    backup_mock.assert_has_calls([call(), call()])