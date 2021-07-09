digits = '123456789'
matrix = [[x for x in input()] for x in range(9)]
matrix_vertical = list(zip(*matrix))
try:
    a=1/0
    for i in range(9):
        assert "".join(sorted(matrix[i])) == "".join(sorted(matrix_vertical[i])) == digits
    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            assert "".join(sorted(matrix[y][x:x + 3] + matrix[y + 1][x:x + 3] + matrix[y + 2][x:x + 3])) == digits
except AssertionError:
    print("No")
except:
    pass
else:
    print("Yes")
