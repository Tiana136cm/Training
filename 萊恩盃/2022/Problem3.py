from collections import Counter
from itertools import product


def f(deck):
    cs = sorted(deck, key=lambda ab: ab[::-1])
    for suit, number in cs:
        if number == 0:
            cs.append((suit, 13))
    print(cs)

    has_straight = False
    for i in range(len(cs) - 4):
        ks = cs[i:i + 5]
        suits, cards = list(zip(*ks))
        if len(set(map(sum, zip(cards, range(4, -1, -1))))) == 1:
            has_straight = True
            if len(set(suits)) == 1:
                return '同花順子'
    return '順子' if has_straight else None


def g(deck):
    suits, numbers = zip(*deck)
    c_suits, c_numbers = Counter(suits), Counter(numbers)
    s_amount, n_amount = list(c_suits.values()), list(c_numbers.values())
    if 4 in n_amount:
        return '鐵支'
    if 3 in n_amount and 2 in n_amount:
        return '葫蘆'
    if 5 in s_amount:
        return '同花'
    if 3 in n_amount:
        return '三條'
    if n_amount.count(2) == 2:
        return '兩對'
    if 2 in n_amount:
        return '一對'
    return '無'


def get_card_repr(card):
    suit, number = card
    
    if number == 0:
        return f'{suit}A'
    if number >= 10:
        return f'{suit}{("J", "Q", "K")[number - 10]}'
    return f'{suit}{number + 1}'
    

mapping = list(product(['梅花', '方塊', '紅心', '黑桃'], range(13)))

deck = list(mapping[x - 1] for x in map(int, input().split()))
res_f = f(deck)
res = res_f if res_f is not None else g(deck)
print(*map(get_card_repr, deck), res, sep='')