"""
Задача 07. Специални числа
Дадени са две цели числа N и M, където N < M.
Намерете всички "специални" числа в диапазона от N до М (включително).
Едно число се нарича "специално" число,
 ако абсолютната разликата между всеки две съседни цифри е 1.

Например:
123 е специално, защото разликата между 1 и 2 е 1,
и разликата между 2 и 3 също е 1.
421 не е специално, защото разликата между 4 и 2 е 2,
 което е по-голямо от 1.
Вход
N – цяло число в диапазона [10…30 000 000]
M – цяло число в диапазона [10…30 000 000]
Изход
Да се отпечатат всички специални числа в диапазона N до М в нарастващ ред, всяко на нов ред.
"""

def generate_special_numbers(current_num, start_num, end_num, result):
    if start_num <= current_num <= end_num:
        result.append(current_num)

    if current_num > end_num:
        return
    last_digit = current_num % 10
    if last_digit > 0:
        next_num = current_num * 10 + (last_digit - 1)
        generate_special_numbers(next_num, start_num, end_num, result)

    if last_digit < 9:
        next_num = current_num * 10 + (last_digit + 1)
        generate_special_numbers(next_num, start_num, end_num, result)

start_num = int(input())
end_num = int(input())
result = []

for start_digit in range(1, 10):
    generate_special_numbers(start_digit, start_num, end_num, result)
result.sort()
for num in result:
    print(num)
