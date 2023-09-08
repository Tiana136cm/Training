from collections import Counter

input()
counter = Counter(map(int, input().strip().split()))
for k, v in sorted(counter.items()):
    print(k, v)
