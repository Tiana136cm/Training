for _ in range(int(input().strip())):
    current_date = input().strip()
    birth_date = input().strip()

    d1, m1, y1 = map(int, current_date.split('/'))
    d2, m2, y2 = map(int, birth_date.split('/'))

    print(y1 - y2 - int(m2 > m1 or m2 == m1 and d2 > d1))
