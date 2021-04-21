import threading
import random

class CheckSomething(threading.Thread):
    def __init__(self, variable):
        super(CheckSomething, self).__init__()
        self.start_flag = threading.Event()
        self.variable = variable

    def check_position(self, variable):
        x = random.randint(100)
        if variable == x:
            self.stop_checking()

    def run(self):
        while True:
            self.check_position(self.variable)

    def stop_checking(self):
        self.start_flag.set()

    def stopped(self):
        return self.start_flag.is_set()