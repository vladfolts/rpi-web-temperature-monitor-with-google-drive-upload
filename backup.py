import storer
import upload

import argparse
import os
from pipes import quote
import subprocess
import sys
import time

def backup(input, output):
    args = ['sqlite3', input, '.backup %s' % output.replace('\\', '\\\\')]
    print('running: %s' % ' '.join([quote(a) for a in args]))
    sys.stdout.flush()
    subprocess.check_call(args)

def with_retry(backup, attempts=5, timeout=0.2):
    retry = 0
    while True:
        try:
            backup()
            return
        except Exception as x:
            retry += 1
            if retry < attempts:
                print('retrying (%d) backup in %s seconds after an error: %s' 
                      % (retry, timeout, x))
                time.sleep(timeout)
            else:
                print('giving up after %d attempts' % attempts)
                raise
        
def backup_and_trim(db_path, upload=upload.upload):
    db_dir, db_name = os.path.split(db_path)
    db = storer.Sqlite3Storer(db_path)
    dates = db.list_dates()
    if dates:
        for date in dates:
            backup_path = os.path.join(db_dir, '%s.db' % date)
            with_retry(lambda: backup(db_path, backup_path))
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
