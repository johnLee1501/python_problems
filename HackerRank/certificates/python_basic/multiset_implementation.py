class Multiset:
    def __init__(self):
        self.multiset = []

    def add(self, val):
        self.multiset.append(val)

    def remove(self, val):
        if val in self.multiset:
            self.multiset.remove(val)

    def __contains__(self, val):
        if val in self.multiset:
            return True
        else:
            return False

    def __len__(self):
        return (len(self.multiset))


if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result


    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(input())
    result = performOperations(operations)
    print('\n'.join(map(str, result)))
