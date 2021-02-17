def validator(s, cmd):
    for c in s:
        if getattr(c, cmd)():
            return True
    return False


if __name__ == '__main__':
    cmds = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']
    s = input()
    for cmd in cmds:
        print(validator(s, cmd))

"""
str = input()
print(any(c.isalnum() for c in str))
print(any(c.isalpha() for c in str))
print(any(c.isdigit() for c in str))
print(any(c.islower() for c in str))
print(any(c.isupper() for c in str))
"""
