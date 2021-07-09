try:
    pass
except IOError as exc:
    print(exc.errno)