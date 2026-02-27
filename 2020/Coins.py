p = int(input())
coins = []
k = 0
while True:
    c1 = 10 ** k
    c2 = 25 * 10 ** k

    if c1 <= p:
        coins.append(c1)
    if c2 <= p:
        coins.append(c2)
    if c1 > p and c2 > p:
        break
    k += 1
coins.sort(reverse=True)
count = 0
remaining = p
for coin in coins:
    if remaining >= coin:
        num = remaining // coin
        count += num
        remaining -= num * coin
print(count)