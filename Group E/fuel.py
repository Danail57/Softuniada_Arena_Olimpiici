n, k, y, a, b = map(int, input().split())
def sum_of_digits(number):
    return sum(int(d) for d in str(number))

total_cost = 0
position = 0
while position < n:
    remaining = n - position
    fuel_km = min(k, remaining)
    if sum_of_digits(position) % y == 0:
        price = b
    else:
        price = a

    total_cost += price * fuel_km
    position += k
print(total_cost)