n, m = map(int, input().split())
field = [list(input()) for _ in range(n)]

player_row = n - 1
player_col = field[player_row].index("S")

k = int(input())
total_jumps = 0
under_player = '0'

for _ in range(k):
    row, steps = map(int, input().split())
    steps %= m
    field[row] = field[row][-steps:] + field[row][:-steps]

    if player_row > 0 and field[player_row - 1][player_col] == "-":
        field[player_row][player_col] = under_player
        player_row -= 1
        under_player = field[player_row][player_col]
        field[player_row][player_col] = "S"
        total_jumps += 1


win = player_row == 0
print("Win" if win else "Lose")
print(f"Total Jumps: {total_jumps}")
for row in field:
    print("".join(row))