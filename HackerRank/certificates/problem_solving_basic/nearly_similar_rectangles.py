from collections import Counter
"""
Por terminar. Aún no es lo suficientemente eficiente"""

def nearlySimilarRectangles(sides):
    rectangles_similars = 0
    # for x in range(len(sides) - 1):
    #     for y in range(x + 1, len(sides)):
    #         if sides[x][0] // sides[y][0] == sides[x][1] // sides[y][1]:
    #             rectangles_similars += 1
    # return rectangles_similars
    size_rectangles = []
    for x in range(len(sides)):
        size_rectangles.append(sides[x][0] / sides[x][1])
    for x in range(len(size_rectangles) - 1):
        for y in range(x + 1, len(size_rectangles)):
            if size_rectangles[x] == size_rectangles[y]:
                rectangles_similars += 1
    return rectangles_similars


if __name__ == '__main__':
    sides_rows = int(input().strip())
    sides_columns = int(input().strip())
    sides = []
    for _ in range(sides_rows):
        sides.append(list(map(int, input().rstrip().split())))
    result = nearlySimilarRectangles(sides)
    print(result)
