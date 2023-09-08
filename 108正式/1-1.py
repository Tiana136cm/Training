from itertools import accumulate


for _ in range(int(input().strip())):
    xs = map(lambda x: int(x == 'O'), input().strip())
    print(sum(accumulate(xs, lambda prev, x: x * (prev + 1))))
