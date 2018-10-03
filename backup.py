import storer

import subprocess

def backup(input=storer.db_name, output='backup.db'):
    subprocess.check_call(['sqlite3', input, '.backup %s' % output.replace('\\', '\\\\')])
