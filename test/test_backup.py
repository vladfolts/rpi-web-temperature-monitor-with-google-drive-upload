import backup
import storer

import os
import pytest

def test_backup(with_empty_dir, with_sample_db):
    output = os.path.join(with_empty_dir, 'backup.db')
    db_path = with_sample_db[1]
    backup.backup(db_path, output)
    assert os.path.exists(output)

def test_backup_can_overwrite_existing_backup(with_empty_dir, with_sample_db):
    test_backup(with_empty_dir, with_sample_db)
    test_backup(with_empty_dir, with_sample_db)

def test_backup_and_trim(with_two_dates_in_sample_db):
    db, db_path = with_two_dates_in_sample_db
    assert db.list_dates() == ['2018-10-14', '2018-09-16']

    uploaded = []
    backup.backup_and_trim(db_path, upload=lambda path: uploaded.append(path))
    assert uploaded == [os.path.join(os.path.dirname(db_path), name) for name in ['2018-10-14.db', '2018-09-16.db']]
    assert db.list_dates() == ['2018-10-14']