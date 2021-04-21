import multiprocessing
import os
import time


def worker():
    PID = os.getpid()
    print("Hello, I am the process with PID %d" % PID)
    time.sleep(20)
    print('Adiós tarea')

if __name__ == '__main__':
    p = multiprocessing.Process(target=worker)
    p.start()
