for _ in range(int(input().strip())):
    n = int(input().strip())
    xs = []
    while n != 1:
        for x in range(9, 1, -1):
            if n % x == 0:
                xs.append(x)
                n //= x
                break
        else:
            print(-1)
            break
    else:
        print(''.join(map(str, reversed(xs))))
