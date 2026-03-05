def count_zeros(number):
    return str(number).count("0")

a = int(input())
b = int(input())
one_zero = 0
two_zeros = 0
three_zeros = 0

for i in range(a, b  + 1):
    zeros = count_zeros(i)
    if zeros == 1:
        one_zero += 1
    elif zeros == 2:
        two_zeros += 1
    elif zeros == 3:
        three_zeros += 1

print(one_zero)
print(two_zeros)
print(three_zeros)
