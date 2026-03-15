def draw_a_house():
    n = int(input())
    width = 2 * n - 1
    for i in range(n):
        left_padding = "." * (n - 1 - i)
        if i == 0:
            print(left_padding + "*" + left_padding)
        elif i == n - 1:
            row = "* " * n
            print(row.strip())
        else:
            print(left_padding + "*" + " " * (2 * i - 1) + "*" + left_padding)
    print("+" + "-" * (width - 2) + "+")

    for _ in range(n - 2):
        print("|" + " " * (width - 2) + "|")

    if n > 1:
        print("+" + "-" * (width - 2) + "+")

draw_a_house()
