partial_map = input()
result = set()

def generate(path, index):
    if index == len(partial_map):
        result.add(path)
        return
    if partial_map[index] == "*":
        for symbol in "SLR":
            generate(path + symbol, index + 1)
    else:
        generate(path + partial_map[index], index + 1)
generate("", 0)
sorted_paths = sorted(result)
print(len(sorted_paths))
for path in sorted_paths:
    print(path)