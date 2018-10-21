import reader

class DeviceStub(object):
    def __init__(self, text):
        self.__text = text

    def read(self):
        return self.__text

    def __enter__(self, *args):
        return self

    def __exit__(self, *args):
        pass

class ReaderStub(object):
    def __init__(self, values):
        self.__values = values
        self.__current_value = 0

    def read(self):
        result = self.__values[self.__current_value]
        self.__current_value += 1
        return result

class TestTemperatureReader(object):
    def test_read(self):
        data = iter([
            '72 01 4b 46 7f ff 0e 10 57 : crc=57 YES\n'\
            '72 01 4b 46 7f ff 0e 10 57 t=23125\n',
            '72 01 4b 46 7f ff 0e 10 57 : crc=57 YES\n'\
            '72 01 4b 46 7f ff 0e 10 57 t=33000\n'
            ])
        r = reader.TemperatureReader(open_device=lambda: DeviceStub(next(data)))
        assert r.read() == 23.125
        assert r.read() == 33

    def test_may_read_none(self):
        data = iter([
            '',
            '72 01 4b 46 7f ff 0e 10 57 t=23125\n',
            '72 01 4b 46 7f ff 0e 10 57 : crc=57 YES\n'\
            '72 01 4b 46 7f ff 0e 10 57 t=33000\n',
            'abc'
            ])
        r = reader.TemperatureReader(open_device=lambda: DeviceStub(next(data)))
        assert r.read() is None
        assert r.read() is None
        assert r.read() == 33
        assert r.read() is None

def test_timed_reader():
    values = [20, 30, 25, 10, 10, 10]
    timeout_seconds = 0.1
    epsilon_t = timeout_seconds / 10
    r = reader.TimedReader(reader=ReaderStub(values), timeout_seconds=timeout_seconds)
    prev_t = None
    for v in values:
        read = r.read()
        assert read['value'] == v
        t = read['time']

        print(read)
        first_sample = prev_t is None
        if first_sample:
            prev_t = t
        else:
            next_t = prev_t + timeout_seconds
            assert abs(t - next_t) < epsilon_t
            prev_t = t