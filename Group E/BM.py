N, M = map(int, input().split())
current = M
total = M
for day in range(2, N + 1):
    current += day
    total += current

print(total)
