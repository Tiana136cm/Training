memo = [1, 1]
for _ in range(int(input().strip())):
    n = int(input().strip())

    if n % 2 == 0:
        print(0)
        continue

    k = n // 2

    if len(memo) > k:
        print(memo[k])

    for i in range(len(memo), k + 1):
        memo.append(sum(memo[j] * memo[i - j - 1] for j in range(i)))

    print(memo[k])
