def stars_in_a_cube():
    n = int(input())
    cube = []
    layers = [[] for _ in range(n)]
    for _ in range(n):
        row_input = input().strip()
        if not row_input:
            continue
        parts = row_input.split('|')
        for i in range(n):
            row_letters = parts[i].split()
            layers[i].append(row_letters)
    total_stars = 0
    star_counts = {}
    for l in range(1, n - 1):
        for r in range(1, n - 1):
            for c in range(1, n - 1):
                center = layers[l][r][c]
                if (layers[l - 1][r][c] == center and
                        layers[l + 1][r][c] == center and
                        layers[l][r - 1][c] == center and
                        layers[l][r + 1][c] == center and
                        layers[l][r][c - 1] == center and
                        layers[l][r][c + 1] == center):
                    total_stars += 1
                    star_counts[center] = star_counts.get(center, 0) + 1
    print(total_stars)
    for char in sorted(star_counts.keys()):
        print(f"{char} -> {star_counts[char]}")
stars_in_a_cube()
