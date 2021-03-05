import re
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        end = time.time()
        print(
            '{} took time {:.4f}'.format(func.__name__, end - start)
        )
        return f

    return wrapper


PATTERN = re.compile(r'^[7-9]\d{9}$')
NUMBERS = [
              '9587456281',
              '1252478965'
          ] * 1000000


@timeit
def test_pre_compiled_pattern():
    for number in NUMBERS:
        if PATTERN.match(number):
            True
        else:
            False


@timeit
def test_every_time_compiled_pattern():
    for number in NUMBERS:
        if re.match(r'^[7-9]\d{9}$', number):
            True
        else:
            False


if __name__ == '__main__':
    test_pre_compiled_pattern()
    test_every_time_compiled_pattern()
