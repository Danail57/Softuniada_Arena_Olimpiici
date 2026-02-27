def generate_permutations(array, left, right, result):
    if left == right:
        result.append(array[:])
    else:
        for i in range(left, right + 1):
            array[left], array[i] = array[i], array[left]
            generate_permutations(array, left + 1, right, result)
            array[left], array[i] = array[i], array[left]

def generate_orientations(sticks, index, current, all_orients):
    if index == len(sticks):
        all_orients.append(current[:])
        return
    x, y = sticks[index]
    current.append((x, y))
    generate_orientations(sticks, index + 1, current, all_orients)
    current.pop()

    if x != y:
        current.append((y, x))
        generate_orientations(sticks, index + 1, current, all_orients)
        current.pop()

n = int(input())
sticks = [tuple(map(int, input().split())) for _ in range(n)]
all_orients = []
generate_orientations(sticks, 0, [], all_orients)
unique_arrangements = set()

for oriented in all_orients:
    perms = []
    generate_permutations(list(oriented), 0, n - 1, perms)
    for p in perms:
        unique_arrangements.add(tuple(p))

sorted_arrangements = sorted(unique_arrangements)
print(len(sorted_arrangements))
for arrangement in sorted_arrangements:
    print(" # ".join(f"|{a}-{b}|" for a, b in arrangement))
