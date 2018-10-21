import glob
import os
import time

def _open_device():
    base_dir = '/sys/bus/w1/devices'
    device_folders = glob.glob(os.path.join(base_dir, '28*'))
    if len(device_folders) == 0:
        raise Exception('cannot find temperature sensor device folder')

    return open(os.path.join(device_folders[0], 'w1_slave'), 'r')

class TemperatureReader(object):
    def __init__(self, open_device=_open_device):
        self.__open_device = open_device 

    def read(self):
        with self.__open_device() as device:
            lines = device.read().splitlines()

        lines_count = len(lines)
        if lines_count < 2:
            print('expected at least 2 lines, got %d' % lines_count)
            return None

        first_line = lines[0]
        if not first_line.endswith('YES'):         
            print('unexpected first line: %s' % first_line)
            return None

        second_line = lines[1]
        t_prefix = 't='
        t_index = second_line.rfind(t_prefix)
        if t_index == -1:
            print('unexpected second line: %s' % second_line)
            return None

        return int(second_line[t_index + len(t_prefix): ]) / 1000.

class TimedReader(object):
    def __init__(self, reader, timeout_seconds):
        self.__reader = reader
        self.__interval = timeout_seconds        
        self.__next_time = time.time() 
    
    def read(self):
        wait_for = self.__next_time - time.time()
        if wait_for > 0:
            time.sleep(wait_for)

        self.__next_time += self.__interval
        result = self.__reader.read()
        return {'time': time.time(), 'value': result}
