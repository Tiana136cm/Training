ranges = sorted(eval(input()))
collapsed = []

i, n = 1, len(ranges)
left, right = ranges[0]
while i < n:
    a, b = ranges[i]
    if a > right:
        collapsed.append([left, right])
        left, right = ranges[i]
    if a <= right and b > right:
        right = b
        
    i += 1
collapsed.append([left, right])

mapping = ['零', '壹', '貳', '參', '肆', '伍', '陸', '柒', '捌', '玖']
def get_repr(lr):
    return f"[{','.join(map(lambda x: ''.join(mapping[int(c)] for c in str(x)), lr))}]"

print(','.join(map(get_repr, collapsed)))