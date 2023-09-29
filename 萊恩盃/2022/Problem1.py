def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


y1, m1, d1 = map(int, input().split('/'))
y2, m2, d2 = map(int, input().split('/'))

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if not is_leap(y1) and m1 == 2 and d1 == 29 or\
        not is_leap(y2) and m2 == 2 and d2 == 29:
    print(-1)
else:
    res = 1
    for y in range(y1, y2 - int(m1 > m2 or m1 == m2 and d1 > d2)):
        res += 365 + int(is_leap(y))

    if m1 > m2:
        for m in range(m1 - 1, 12):
            # 1 instead of 2 here because days start from 0
            res += days[m] + int(m == 1 and is_leap(y1))
        for m in range(m2 - 1):
            res += days[m] + int(m == 1 and is_leap(y2))
    else:
        for m in range(m1 - 1, m2 - 1):
            res += days[m] + int(m == 1 and is_leap(y2))

    res += d2 - d1
    print(res)
