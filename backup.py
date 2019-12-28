import storer
import upload

import argparse
import os
import subprocess
import time

def backup(input, output):
    max_retry = 5
    retry = 0
    timeout = 0.2
    while True:
        rc = subprocess.call(['sqlite3', input, '.backup %s' % output.replace('\\', '\\\\')])
        if rc == 0:
            break
        
        retry += 1
        if retry == max_retry:
            raise Exception('cannot backup database (exit code: %d) affter %d attempts, giving up'
                            % (rc, max_retry))
        print('cannot backup database (exit code: %d), retrying (%d) in %s seconds...' 
                % (rc, retry, timeout))
        time.sleep(0.1)

def backup_and_trim(db_path, upload=upload.upload):
    db_dir, db_name = os.path.split(db_path)
    db = storer.Sqlite3Storer(db_path)
    dates = db.list_dates()
    if dates:
        for date in dates:
            backup_path = os.path.join(db_dir, '%s.db' % date)
            backup(db_path, backup_path)
            backup_db = storer.Sqlite3Storer(backup_path)
            backup_db.trim(date)
            backup_db.close()
            print('uploading "%s"' % backup_path)
            upload(backup_path)

        db.trim(dates[0], before_only=True)

def process_command_line():
    parser = argparse.ArgumentParser(description='Backups and trims database.')
    parser.add_argument('--db-path', dest='db_path', default=storer.db_name,
                        help='full path to db')
    return parser.parse_args()

if __name__ == '__main__':
    options = process_command_line()
    backup_and_trim(options.db_path)
