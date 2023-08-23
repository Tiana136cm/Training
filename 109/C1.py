for _ in range(int(input().strip())):
    s = input().strip()
    n = int(s)
    while s != s[::-1]:
        n += int(s[::-1])
        s = str(n)
    print(s)
