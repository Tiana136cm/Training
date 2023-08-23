for _ in range(int(input().strip())):
    xs = list(map(int, input().strip().split()))
    n = len(xs)
    for i in range(1, n):
        if xs[i - 1] > 0:
            xs[i] += xs[i - 1]
    print(max(xs))
