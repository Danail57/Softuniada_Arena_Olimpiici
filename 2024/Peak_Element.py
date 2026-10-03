"""
Задача 01. Върхов елемент
Напишете програма, която получава поредица от цели числа, разделени
с интервал. Намерете "върховия елемент" в дадената поредица.
"Върхов елемент" е този, който е по-голям от съседите си.
Пример: Поредицата от цели числа 3 6 9 2 4, върховият елемент е 9,
защото е по-голям от съседите си 6 и 2.
Забележка 1: Ако в една поредица намерите два или повече върхови
 елемента, отпечатайте този, който е с най-голяма стойност.
Забележка 2: Няма да има случай, в който да не може да се
намери върхов елемент или той да не е наличен.
"""

def find_highest_peak():
    numbers = list(map(int, input().split()))
    max_peak = None

    for number in range(1, len(numbers) - 1):
        current = numbers[number]
        left_neighbour = numbers[number - 1]
        right_neighbour = numbers[number + 1]

        if current > left_neighbour and current > right_neighbour:
            if max_peak is None or current > max_peak:
                max_peak = current
    print(max_peak)
find_highest_peak()
