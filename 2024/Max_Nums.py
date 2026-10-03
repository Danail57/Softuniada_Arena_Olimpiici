"""
Напишете програма, която получава масив от цели числа, разделени с
интервал и цяло число K (брой на най-големите числа). Намерете K на
брой от най-големите стойности на масива от цели числа.
Пример: Нека кажем, че K = 4, това означава, че трябва да намерим
четирите най-големи числа от масива.

Пример
[23 67 34 12 39 27]
K = 4
=> 67 39 34 27

"""

def max_numbers():
    numbers = list(map(int, input("Write some numbers: ").split()))
    count_numbers_to_take_from_array = int(input("How many numbers you want to take? "))
    numbers.sort(reverse=True)
    count_numbers_to_take_from_array = numbers[:count_numbers_to_take_from_array]
    print(*count_numbers_to_take_from_array)
max_numbers()
