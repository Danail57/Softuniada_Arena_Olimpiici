n = int(input())
values = list(map(int, input().split()))

cards = list(range(1, n + 1))
for x in values:
    first = cards[:x]
    second = cards[x:]
    shuffled = []

    min_len = min(len(first), len(second))
    for i in range(min_len):
        shuffled.append(first[i])
        shuffled.append(second[i])
    shuffled.extend(first[min_len:])
    shuffled.extend(second[min_len:])
    cards = shuffled
print(*cards)