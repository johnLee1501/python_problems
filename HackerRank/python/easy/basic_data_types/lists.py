if __name__ == '__main__':
    N = int(input())
    a = []
    for _ in range(N):
        cmd, *args = input().split()
        args = list(map(int, args))
        if cmd == 'print':
            print(a)
        else:
            getattr(a, cmd)(*args)
