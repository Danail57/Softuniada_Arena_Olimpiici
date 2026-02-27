size = int(input())
height = size + (size // 2)

for i in range(height):
    for j in range(size):
        if (i + j) % 4 == 0:
            print("#", end='')
        else:
            print(".", end='')
    print()

