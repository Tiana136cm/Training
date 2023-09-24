from math import ceil, sqrt


def is_prime(k):
    a = int(ceil(sqrt(k)))
    return not any(k % i == 0 for i in range(2, a + 1))


for k in map(int, iter(input, '0')):
    print(sum(1 for i in range(2, k // 2 + 1) if is_prime(i) and is_prime(k - i)))
