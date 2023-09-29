from itertools import combinations, starmap
from math import inf, sqrt


def collinear(p1, p2, p3):
    (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
    return (y1 - y3) / (x1 - x3) == (y1 - y2) / (x1 - x2)


def calc_h(p1, p2, p3):
    (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
    numerator = ((x1**2 - x2**2 + y1**2 - y2**2) * (y1 - y3)) - (x1**2 - x3**2 + y1**2 - y3**2) * (y1 - y2)
    denominator = 2 * ((x1 - x2) * (y1 - y3) - (x1 - x3) * (y1 - y2))
    return numerator / denominator


def calc_k(p1, p2, p3):
    (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
    numerator = (x1 ** 2 - x2**2 + y1**2 - y2**2) * (x1 - x3) - (x1**2 - x3**2 + y1**2 - y3**2) * (x1 - x2)
    denominator = 2 * ((x1 - x3) * (y1 - y2) - (x1 - x2) * (y1 - y3))
    return numerator / denominator


def calc_r(h, k, p):
    x, y = p
    return sqrt((x - h)**2 + (y - k)**2)


points = []
for _ in range(4):
    points.append(tuple(map(float, input().split())))
    
combs = list(combinations(points, 3))
if any(starmap(collinear, combs)):
    print('無解')
else:
    h, k, p = min((calc_h(*ps), calc_k(*ps), ps[0]) for ps in combs)
    r = calc_r(h, k, p)
    print(h, k, r)
    