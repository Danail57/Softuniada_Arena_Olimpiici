k = int(input())
n = int(input())

array = [int(input()) for _ in range(n)]
array.sort()
min_diff = float("inf")
for i in range(n - k + 1):
    current_diff = array[i + k - 1] - array[i]
    if current_diff < min_diff:
        min_diff = current_diff
print(min_diff)