# 0 H 1 M 2 L
AND = [
    [0, 0, 2],
    [0, 1, 2],
    [2, 2, 2],
]

OR = [
    [0, 0, 0],
    [0, 1, 2],
    [0, 2, 2],
]

XOR = [
    [2, 1, 0],
    [1, 2, 1],
    [0, 1, 2],
]

XAND = [
    [0, 2, 2],
    [2, 0, 2],
    [2, 2, 0],
]

FUZZY = [
    [0, 1, 1],
    [1, 1, 1],
    [1, 1, 2],
]

mapping = ['H', 'M', 'L']

a, b = map(float, input().split())
if a < 0 or b < 0 or not a.is_integer() or not b.is_integer():
    print('輸入數值錯誤')
else:
    a, b = int(a) % 3, int(b) % 3

    res = []
    for f in [AND, OR, XOR, XAND, FUZZY]:
        res.append(f[a][b])
    
    print(''.join(mapping[x] for x in res))