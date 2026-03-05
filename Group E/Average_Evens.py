def average_even_numbers(m, n):
    total = 0
    count = 0
    for number in range(m, n + 1):
        if number % 2 == 0:
            total += number
            count += 1
    if count == 0:
        return 0
    return int (total / count)

m = int(input())
n = int(input())
print(average_even_numbers(m, n))
