
"""
Жоро найстина обича числа, но според него някои числа са
 по-готини от други, помогни на Жоро да напише програма да
 класифицира числа. Според Жоро числата се класифицират по 3 условия:
- Дали са нечетни
- Дали са отрицателни
- Дали се делят без остатък на неговото любимо число
Според 3те условия Жоро класифицира числата така:
- Ако едно число не спазва нито едно от условията
(не е нечетно, не е отрицателно и не се дели без остатък
 на любимото му число) то Жоро мисли че числото е “boring”
- Ако числото спазва само едно от условията, то Жоро смята че
 е “awesome”
- Ако числото спазва 2 от условията, то е “super awesome”
- Ако числото спазва всичките 3 условия, то то е “super special awesome”
"""

number = int(input())
favourite_number = int(input())

is_odd = number % 2 != 0
is_negative = number < 0
is_divisible = number % favourite_number == 0

if not is_odd and not is_negative and not is_divisible:
    print("boring")

elif (is_odd and not is_negative and not is_divisible) or \
     (not is_odd and is_negative and not is_divisible) or \
     (not is_odd and not is_negative and is_divisible):
    print("awesome")

elif (is_odd and is_negative and not is_divisible) or \
     (is_odd and not is_negative and is_divisible) or \
     (not is_odd and is_negative and is_divisible):
    print("super awesome")

elif is_odd and is_negative and is_divisible:
    print("super special awesome")
