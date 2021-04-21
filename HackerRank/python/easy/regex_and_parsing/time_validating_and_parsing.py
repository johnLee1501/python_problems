import email.utils
import time
import re


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


@timeit
def recompile(emails_parse):
    pattern = re.compile(r'^[A-Za-z][\w\-\.]+\@[A-Za-z]+\.[A-Za-z]{1,3}$')
    for email_parse in emails_parse:
        if pattern.match(email_parse[1]):
            pass


@timeit
def not_recompile(emails_parse):
    pattern = r'^[A-Za-z][\w\-\.]+\@[A-Za-z]+\.[A-Za-z]{1,3}$'
    for email_parse in emails_parse:
        if re.match(pattern, email_parse[1]):
            pass


if __name__ == '__main__':
    n = int(input())
    emails_parse = [email.utils.parseaddr(input()) for _ in range(n)] * 300000
    recompile(emails_parse)
    not_recompile(emails_parse)
