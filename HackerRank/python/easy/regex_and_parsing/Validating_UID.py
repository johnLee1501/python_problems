"""
import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')"""

# Solution 3
import re

for _ in range(int(input())):
    s = input()
    print('Valid' if all(
        [re.search(r, s) for r in [r'[A-Za-z0-9]{10}', r'([A-Z].*){2}', r'([0-9].*){3}']])
                     and not re.search(r'.*(.).*\1', s) else 'Invalid')
