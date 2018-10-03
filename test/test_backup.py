import backup
import storer

import os
import pytest

def test_backup(with_empty_dir, with_sample_db):
    output = os.path.join(with_empty_dir, 'backup.db')
    backup.backup(with_sample_db, output)
    assert os.path.exists(output)