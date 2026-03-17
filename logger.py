from time import sleep
import storer
import reader

import argparse
import random

def run(read, store):
    next_attempt_interval = 1  # seconds
    while True:
        try:
            data = read.read()
            store.put(storer.Record(timestamp=data['time'], value=data['value']))
            next_attempt_interval = 1
        except Exception as e:
            print('Error: %s' % e)            
            if next_attempt_interval < 600:
                next_attempt_interval *= 2
            print('Next attempt in %d seconds' % next_attempt_interval)
            sleep(next_attempt_interval)

class _RandomReader(object):
    def read(self):
        return random.randint(0, 30)

def process_command_line():
    parser = argparse.ArgumentParser(description='Logs temperature.')
    parser.add_argument('--random-reader', dest='random_reader', action='store_true',
                        help='do not read actual temerature, use randomizer')
    parser.add_argument('--db-path', dest='db_path', default=storer.db_name,
                        help='full path to db')
    return parser.parse_args()

if __name__ == '__main__':
    options = process_command_line()
    t_reader = _RandomReader() if options.random_reader else reader.TemperatureReader()

    s = storer.Sqlite3Storer(options.db_path)
    r = reader.TimedReader(reader=t_reader, timeout_seconds=1)
    run(r, s)
