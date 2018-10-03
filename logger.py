import storer
import reader

def run(read, store):
    while True:
        data = read.read()
        store.put(storer.Record(timestamp=data['time'], value=data['value']))

if __name__ == '__main__':
    s = storer.Sqlite3Storer()
    r = reader.TimedReader(reader=reader.TemperatureReader(), timeout_seconds=1)
    run(r, s)
