memo = [1, 1]
for _ in range(int(input().strip())):
    n = int(input().strip())

    if n % 2 == 0:
        print(0)
        continue

    k = n // 2  # 在左邊的node數
    # 左邊的樹的排列對到一個獨一無二的右邊樹的排列: 對射(bijection)

    if len(memo) > k:
        print(memo[k])

    for i in range(len(memo), k + 1):
        # 排列組合: 左邊的node亂排 * 右邊的node亂排
        memo.append(sum(memo[j] * memo[i - j - 1] for j in range(i)))

    print(memo[k])
