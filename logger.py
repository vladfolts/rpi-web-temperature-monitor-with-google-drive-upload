import storer
import reader

def run(read, store):
	while True:
		store(read())

if __name__ == '__main__':
    s = storer.Sqlite3Storer('data.db')
    r = reader.TimedReader(reader=reader.TemperatureReader(), timeout_seconds=1)
    run(lambda: r.read(), 
        lambda data: s.put(storer.Record(timestamp=data['time'], value=data['value'])))
