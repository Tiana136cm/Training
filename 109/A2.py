for _ in range(int(input().strip())):
    s = input().strip()
    x = ''.join('1' if c == '4' else '0' for c in s).lstrip('0')
    print(int(s) - int(x), x)
