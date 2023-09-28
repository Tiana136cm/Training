from math import ceil, sqrt


def is_prime(k):
    # all(k % i != 0 for i in range(2, int(ceil(sqrt(k))) + 1))
    # but all number that is not equal to 0 is true, thus `!= 0` can be omitted
    return k == 2 or all(k % i for i in range(2, int(ceil(sqrt(k))) + 1))


for k in map(int, iter(input, '0')):
    print(sum(1 for i in range(2, k // 2 + 1) if is_prime(i) and is_prime(k - i)))
