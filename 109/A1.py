for _ in range(int(input().strip())):
    xs = sorted(map(int, input().strip().split()), reverse=True)
    print(*xs[:2])
