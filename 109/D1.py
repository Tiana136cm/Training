import sys


for line in sys.stdin.readlines():
    n, _, *xs = list(map(int, line.strip().split()))
    dp = [0] * (n + 1)

    for x in xs:
        for m in range(n, x - 1, -1):
            dp[m] = max(dp[m], dp[m - x] + x)

    print(dp[-1])
