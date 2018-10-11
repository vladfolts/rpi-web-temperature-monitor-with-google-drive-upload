import backup
import storer

import os
import pytest

def test_backup(with_empty_dir, with_sample_db):
    output = os.path.join(with_empty_dir, 'backup.db')
    db_path = with_sample_db[1]
    backup.backup(db_path, output)
    assert os.path.exists(output)